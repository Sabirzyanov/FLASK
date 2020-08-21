document.addEventListener('DOMContentLoaded', function() {
    let hardwareBlocks = document.querySelectorAll('.js-hardware-block');
    
    let motherboardBlock = document.querySelector('.origin-motherboard').innerHTML,
        cpuBlock = document.querySelector('.origin-cpu').innerHTML,
        ramBlock = document.querySelector('.origin-ram').innerHTML,
        gpuBlock = document.querySelector('.origin-gpu').innerHTML,
        hddBlock = document.querySelector('.origin-hdd').innerHTML,
        psBlock = document.querySelector('.origin-ps').innerHTML,
        caseBlock = document.querySelector('.origin-case').innerHTML;
    
    hardwareBlocks.forEach(function(item){

      item.addEventListener('click', function(e) {

         e.preventDefault();
         let content = item.querySelector('.container').innerHTML
         let hardwareBlockClass = item.classList[1];
         let originBlock = document.querySelector('.origin-' + hardwareBlockClass);
         originBlock.innerHTML = content;
         let closeButton = document.createElement('div');
         closeButton.addEventListener('click', function(e) {
             let originBlockClass = originBlock.classList[3];
             
             if (originBlockClass == 'origin-motherboard'){
                 originBlock.innerHTML = motherboardBlock;
             }
             
             if (originBlockClass == 'origin-cpu'){
                 originBlock.innerHTML = cpuBlock;
             }
             
             if (originBlockClass == 'origin-gpu'){
                 originBlock.innerHTML = gpuBlock;
             }
             
             if (originBlockClass == 'origin-ram'){
                 originBlock.innerHTML = ramBlock;
             }
             
             if (originBlockClass == 'origin-hdd'){
                 originBlock.innerHTML = hddBlock;
             }
             
             if (originBlockClass == 'origin-ps'){
                 originBlock.innerHTML = psBlock;
             }
             
             if (originBlockClass == 'origin-case'){
                 originBlock.innerHTML = caseBlock;
             }
             
              
         });
         closeButton.innerHTML = '<div class="close-container"><div class="leftright"></div><div class="rightleft"></div></div>';
         let originBlockHeight = originBlock.offsetHeight;
         closeButton.style.marginTop = originBlockHeight * 0.29 + "px";
         originBlock.querySelector('.hardware-close-div').style.height = originBlockHeight + "px"; 
         originBlock.querySelector('.hardware-close-div').style.display = "block";
         originBlock.querySelector('.hardware-close-div').appendChild(closeButton);
         
         $(window).resize(function(e) {
             
             closeButton.style.marginTop = originBlock.offsetHeight * 0.29 + "px";
             originBlock.querySelector('.hardware-close-div').style.height = originBlock.offsetHeight + "px"; 
             
         });
  
          
         let overlay = document.querySelector('.js-overlay-modal');
         modalElem = document.querySelector('.modal[data-modal="' + hardwareBlockClass + '"]');

         modalElem.classList.remove('active');
         overlay.classList.remove('active');
 
      });
      

   });
    
}); 
