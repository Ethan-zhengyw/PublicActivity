(function(){
  var onDrag;
  onDrag = function(control, cb){
    var dragging, lastX, lastY;
    dragging = false;
    lastX = 0;
    lastY = 0;
    control.on('mousedown', function(e){
      dragging = true;
      lastX = e.clientX;
      lastY = e.clientY;
      $(document).on('mousemove.image-cropper-drag', function(e){
        var movementX, movementY;
        if (dragging) {
          movementX = e.clientX - lastX;
          movementY = e.clientY - lastY;
          lastX = e.clientX;
          lastY = e.clientY;
          cb(movementX, movementY);
        }
      });
      $(document).on('mouseup', function(){
        dragging = false;
        $(document).off('mousemove.image-cropper-drag');
      });
    });
  };
  $(function(){
    $('image-cropper').each(function(){
      var container, input, preview, cropping, mask, maskCenter, maskLeft, maskRight, maskTop, maskBottom, cropXInput, cropYInput, cropWidthInput, cropHeightInput, imgWidth, imgHeight, containerWidth, containerHeight, containerWidthDivHeight, previewWidth, previewHeight, previewWidthDivHeight, croppingX, croppingY, croppingWidth, croppingHeight, maskX, maskY, maskWidth, maskHeight, newMaskX, newMaskY, newMaskWidth, newMaskHeight, name, setMask;
      container = $(this);
      input = $(container.attr('input'));
      preview = $(container.attr('preview'));
      cropping = container.find('.image-cropper-cropping');
      mask = container.find('.image-cropper-mask');
      maskCenter = container.find('.image-cropper-mask-center');
      maskLeft = container.find('.image-cropper-mask-left');
      maskRight = container.find('.image-cropper-mask-right');
      maskTop = container.find('.image-cropper-mask-top');
      maskBottom = container.find('.image-cropper-mask-bottom');
      cropXInput = container.find('.image-cropper-crop-x');
      cropYInput = container.find('.image-cropper-crop-y');
      cropWidthInput = container.find('.image-cropper-crop-width');
      cropHeightInput = container.find('.image-cropper-crop-height');
      imgWidth = 0;
      imgHeight = 0;
      containerWidth = container.width();
      containerHeight = container.height();
      containerWidthDivHeight = containerWidth / containerHeight;
      previewWidth = preview.width();
      previewHeight = preview.height();
      previewWidthDivHeight = previewWidth / previewHeight;
      croppingX = 0;
      croppingY = 0;
      croppingWidth = 0;
      croppingHeight = 0;
      maskX = 0;
      maskY = 0;
      maskWidth = 0;
      maskHeight = 0;
      newMaskX = 0;
      newMaskY = 0;
      newMaskWidth = 0;
      newMaskHeight = 0;
      name = input.attr('name');
      cropXInput.attr('name', "image-cropper-" + name + "-crop-x");
      cropYInput.attr('name', "image-cropper-" + name + "-crop-y");
      cropWidthInput.attr('name', "image-cropper-" + name + "-crop-width");
      cropHeightInput.attr('name', "image-cropper-" + name + "-crop-height");
      setMask = function(){
        var previewBackgroundDivPreview, previewBackgroundWidth, previewBackgroundHeight, previewBackgroundX, previewBackgroundY;
        if (newMaskX >= croppingX && newMaskX + newMaskWidth <= croppingX + croppingWidth && newMaskY >= croppingY && newMaskY + newMaskHeight <= croppingY + croppingHeight && newMaskWidth > 0 && newMaskHeight > 0) {
          maskX = newMaskX;
          maskY = newMaskY;
          maskWidth = newMaskWidth;
          maskHeight = newMaskHeight;
          mask.css('left', maskX + "px");
          mask.css('top', maskY + "px");
          mask.css('width', maskWidth + "px");
          mask.css('height', maskHeight + "px");
          previewBackgroundDivPreview = previewWidth / maskWidth;
          previewBackgroundWidth = croppingWidth * previewBackgroundDivPreview;
          previewBackgroundHeight = croppingHeight * previewBackgroundDivPreview;
          previewBackgroundX = -(maskX - croppingX) * previewBackgroundDivPreview + croppingX;
          previewBackgroundY = -(maskY - croppingY) * previewBackgroundDivPreview;
          preview.css('background-position', previewBackgroundX + "px " + previewBackgroundY + "px");
          preview.css('background-size', previewBackgroundWidth + "px " + previewBackgroundHeight + "px");
          cropXInput.val(parseInt((maskX - croppingX) / croppingWidth * imgWidth));
          cropYInput.val(parseInt((maskY - croppingY) / croppingHeight * imgHeight));
          cropWidthInput.val(parseInt(maskWidth / croppingWidth * imgWidth));
          cropHeightInput.val(parseInt(maskHeight / croppingHeight * imgHeight));
        }
      };
      onDrag(maskCenter, function(movementX, movementY){
        newMaskX = maskX + movementX;
        newMaskY = maskY + movementY;
        newMaskWidth = maskWidth;
        newMaskHeight = maskHeight;
        setMask();
      });
      onDrag(maskLeft, function(movementX, movementY){
        newMaskX = maskX + movementX;
        newMaskY = maskY;
        newMaskWidth = maskWidth - movementX;
        newMaskHeight = maskHeight - movementX / previewWidthDivHeight;
        setMask();
      });
      onDrag(maskRight, function(movementX, movementY){
        newMaskX = maskX;
        newMaskY = maskY;
        newMaskWidth = maskWidth + movementX;
        newMaskHeight = maskHeight + movementX / previewWidthDivHeight;
        setMask();
      });
      onDrag(maskTop, function(movementX, movementY){
        newMaskX = maskX;
        newMaskY = maskY + movementY;
        newMaskHeight = maskHeight - movementY;
        newMaskWidth = maskWidth - movementY * previewWidthDivHeight;
        setMask();
      });
      onDrag(maskBottom, function(movementX, movementY){
        newMaskX = maskX;
        newMaskY = maskY;
        newMaskHeight = maskHeight + movementY;
        newMaskWidth = maskWidth + movementY * previewWidthDivHeight;
        setMask();
      });
      input.change(function(){
        var reader;
        reader = new FileReader;
        reader.readAsDataURL(this.files[0]);
        reader.onload = function(){
          var img, croppingWidthDivHeight;
          img = document.createElement('img');
          img.setAttribute('src', this.result);
          document.body.appendChild(img);
          imgWidth = img.clientWidth;
          imgHeight = img.clientHeight;
          document.body.removeChild(img);
          croppingWidthDivHeight = imgWidth / imgHeight;
          if (croppingWidthDivHeight > containerWidthDivHeight) {
            croppingWidth = containerWidth;
            croppingHeight = croppingWidth / croppingWidthDivHeight;
            croppingX = 0;
            croppingY = (containerHeight - croppingHeight) / 2;
          } else {
            croppingHeight = containerHeight;
            croppingWidth = croppingHeight * croppingWidthDivHeight;
            croppingY = 0;
            croppingX = (containerWidth - croppingWidth) / 2;
          }
          cropping.css('background-image', "url(" + this.result + ")");
          cropping.css('background-position', croppingX + "px " + croppingY + "px");
          cropping.css('background-size', croppingWidth + "px " + croppingHeight + "px");
          preview.css('background-image', "url(" + this.result + ")");
          preview.css('background-repeat', "no-repeat");
          mask.css('display', 'block');
          if (previewWidthDivHeight > croppingWidthDivHeight) {
            newMaskWidth = croppingWidth;
            newMaskHeight = newMaskWidth / previewWidthDivHeight;
            newMaskX = croppingX;
            newMaskY = (croppingHeight - newMaskHeight) / 2 + croppingY;
          } else {
            newMaskHeight = croppingHeight;
            newMaskWidth = newMaskHeight * previewWidthDivHeight;
            newMaskY = croppingY;
            newMaskX = (croppingWidth - newMaskWidth) / 2 + croppingX;
          }
          setMask();
        };
      });
    });
  });
}).call(this);
