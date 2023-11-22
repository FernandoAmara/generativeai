import os
import base64
import requests
from PIL import Image
from io import BytesIO
from flask import Flask, render_template, request, jsonify
from diffusers import StableDiffusionPipeline, EulerDiscreteScheduler
import torch

app = Flask(__name__, template_folder='templates')

def img_to_base64(img):
    """
       Convert from PIL image format to Base64 
    """
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    return f"data:image/jpeg;base64,{base64.b64encode(buffered.getvalue()).decode('utf-8')}"

@app.route("/")
def web_client():
    """
        Route default '/': Renderize the HTML form
    """
    return render_template('web_client.html')

@app.route('/api')
def api():
    try:
        device = "cuda" if torch.cuda.is_available() else "cpu"

        prompt = request.args.get('prompt')
        negative_prompt = request.args.get('negative_prompt')
        pretrained_model_or_path = "stabilityai/stable-diffusion-2-1-base"
        num_images_per_prompt = int(request.args.get('number_images'))
        num_inference_steps = int(request.args.get('inference_steps'))
        height = int(request.args.get('height'))
        width = int(request.args.get('width'))
        seed = int(request.args.get('seed'))
        guidance_scale = 8
        
        scheduler = EulerDiscreteScheduler.from_pretrained(pretrained_model_or_path, subfolder="scheduler")
        pipeline = StableDiffusionPipeline.from_pretrained(pretrained_model_or_path, scheduler=scheduler).to(device)
        
        generator = torch.Generator(device=device).manual_seed(seed)
        image = pipeline(prompt=prompt, num_images_per_prompt=num_images_per_prompt,
                           negative_prompt=negative_prompt,
                           num_inference_steps=num_inference_steps,
                           height=height, width=width,
                           guidance_scale=guidance_scale,
                           generator=generator)
        
        response = {'images': []}
    
        for img in image['images']:
            img_str = img_to_base64(img)
            response['images'].append(img_str)

    except Exception as e:
        response = f"Oh no, I'm sorry! Error: {e}"
    return jsonify(response)
