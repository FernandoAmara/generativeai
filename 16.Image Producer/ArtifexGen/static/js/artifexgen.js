function startLoading(){
  $("#btn-generate").html('<i class="bi bi-stopwatch-fill"></i> Loading...').prop('disabled', true);
}

function stopLoading(){
  $("#btn-generate").html('<i class="bi bi-arrow-right-circle-fill"></i> Generate').prop('disabled', false);
}

function convertFormToJSON(form){
    const array = $(form).serializeArray();
    const json = {};
    $.each(array, function () {
      json[this.name] = this.value || "";
    });
    return json;
}

function imageWidgetRenderize(base64Img){
  let widgetHTML = `<div class="col-xs-6 col-sm-6 col-md-3 col-lg-3 mt-2">
                      <div class="card">
                        <div class="card-body">
                          <img src="${base64Img}" class="rounded img-fluid img-thumbnail">
                        </div>
                        <div class="card-footer text-center">
                            <a download="image.jpeg" href="${base64Img}" class="btn btn-outline-success w-100">
                              <i class="bi bi-download"></i> Download
                            </a>
                        </div>
                      </div>
                    </div>`;
  $("#output-container").append(widgetHTML)
}

function goGenerate(form){
  $("#output-container").empty();
  console.log(form.valid());
  if(form.valid()){
      startLoading();
      $.getJSON('/api', 
        convertFormToJSON(form)
      , function(data) {
        $.each(data.images, function( index, value ) {
          imageWidgetRenderize(value);
        });
        stopLoading();
      });
  }else{
    alert("Oops!\n I'm sorry, but I couldn't submit your form.\n Enter all inputs data and try again.");
  }
}