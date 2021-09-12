function makeDraggable(evt) {
    var svg = evt.target;
    svg.addEventListener('mousedown', startDrag);
    svg.addEventListener('mousemove', drag);
    svg.addEventListener('mouseup', endDrag);
    svg.addEventListener('mouseleave', endDrag);
    svg.addEventListener('mousemove', showTooltip);

    var destx;
    var desty;
    
    //var selectedElement = false;
    var selectedElement, offset, transform;
    var allowDrop = false;

    var tooltip = document.getElementById('tooltip');
    //var triggers = document.getElementsByClassName('draggable');

    //for (var i = 0; i < triggers.length; i++) {
    //  triggers[i].addEventListener('mousemove', showTooltip);
    //  triggers[i].addEventListener('mouseout', hideTooltip);
    //}

  function startDrag(evt) {

    if (evt.target.classList.contains('draggable')) {
      selectedElement = evt.target;
      offset = getMousePosition(evt);
      // Get all the transforms currently on this element
      var transforms = selectedElement.transform.baseVal;
      // Ensure the first transform is a translate transform
      if (transforms.length === 0 ||
          transforms.getItem(0).type !== SVGTransform.SVG_TRANSFORM_TRANSLATE) {
        // Create an transform that translates by (0, 0)
        var translate = svg.createSVGTransform();
        translate.setTranslate(0, 0);
        // Add the translation to the front of the transforms list
        selectedElement.transform.baseVal.insertItemBefore(translate, 0);
      }
      // Get initial translation amount
      transform = transforms.getItem(0);
      offset.x -= transform.matrix.e;
      offset.y -= transform.matrix.f;

      var coord = getMousePosition(evt);
      tooltip.setAttributeNS(null, "visibility", "visible");
      tooltip.setAttributeNS(null, "x", coord.x+10);
      tooltip.setAttributeNS(null, "y", coord.y+10);
    }
  }
    
   function drag(evt) {
       if (selectedElement) {
            evt.preventDefault();
      var coord = getMousePosition(evt);
      transform.setTranslate(coord.x - offset.x, coord.y - offset.y);
      document.getElementById('info-panel').innerHTML = (coord.x - offset.x) +","+ (coord.y - offset.y);
      destx = selectedElement.getAttribute('dest_x');
      desty = selectedElement.getAttribute('dest_y');
      areWeThere(coord,destx,desty);
      tooltip.setAttributeNS(null, "visibility", "visible");
      tooltip.setAttributeNS(null, "x", coord.x+10);
      tooltip.setAttributeNS(null, "y", coord.y+10);

         //if (coord.x > 500 && coord.y > 500) {allowDrop = true;} 
    }
  }
  
  //function to drop and lock the piece to the empty space
  
    function areWeThere(coord) 
    {
      var tolerance = 10;
      var x = coord.x - offset.x - destx;
      var y = coord.y - offset.y - desty;
  
        if ((x <= tolerance) && (y <= tolerance))
      {allowDrop = true;} 
      else {allowDrop= false;}
      //alert (allowDrop);
    }
    
    function endDrag(evt) {
      tooltip.setAttributeNS(null, "visibility", "hidden");
     if (allowDrop)
     {
       transform.setTranslate(destx,desty);
       selectedElement = null;
     }
     else
     {
      transform.setTranslate(0,0);
      selectedElement = null;
     }
     
    }
    
    function getMousePosition(evt) {
    var CTM = svg.getScreenCTM();
    return {
      x: (evt.clientX - CTM.e) / CTM.a,
      y: (evt.clientY - CTM.f) / CTM.d
    };
  }
  
  function showTooltip(evt) {
    var coord = getMousePosition(evt);
    tooltip.setAttributeNS(null, "visibility", "visible");
    tooltip.setAttributeNS(null, "x", coord.x+10);
    tooltip.setAttributeNS(null, "y", coord.y+10);
    tooltip.firstChild.data = evt.target.getAttributeNS(null, "title");
  }
   }
