document.addEventListener('DOMContentLoaded', function() {
    var hardwareBlocks = document.querySelectorAll('.js-hardware-block');
    
    hardwareBlocks.forEach(function(item){

      item.addEventListener('click', function(e) {

         e.preventDefault();
         var content = item.querySelector('.container').innerHTML
         var hardwareBlockClass = item.classList[1];
         var originBlock = document.querySelector('.origin-' + hardwareBlockClass);
         originBlock.innerHTML = content;
          
         var overlay = document.querySelector('.js-overlay-modal');
         modalElem = document.querySelector('.modal[data-modal="' + hardwareBlockClass + '"]');

         modalElem.classList.remove('active');
         overlay.classList.remove('active');
 
      }); 

   });
    
}); 