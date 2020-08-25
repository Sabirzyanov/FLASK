document.addEventListener('DOMContentLoaded', function() {
    let hardwareBlocks = document.querySelectorAll('.js-hardware-block');
    
    let motherboardBlock = document.querySelector('.origin-motherboard').innerHTML,
        cpuBlock = document.querySelector('.origin-cpu').innerHTML,
        ramBlock = document.querySelector('.origin-ram').innerHTML,
        gpuBlock = document.querySelector('.origin-gpu').innerHTML,
        hddBlock = document.querySelector('.origin-hdd').innerHTML,
        psBlock = document.querySelector('.origin-ps').innerHTML,
        caseBlock = document.querySelector('.origin-case').innerHTML;
    let motherboard = '',
        cpu = '',
        gpu = '',
        ram = '',
        hdd = '',
        ps = '',
        pcCase = '',
        configurationName = '';
    
    hardwareBlocks.forEach(function(item){

      item.addEventListener('click', function(e) {

         e.preventDefault();
         let content = item.querySelector('.container').innerHTML;
         
         let hardwareBlockClass = item.classList[1];
         let hardwarePrice = item.querySelector('.hardware-price');
         hardwarePrice.classList.add('choosed');
          
         let originBlock = document.querySelector('.origin-' + hardwareBlockClass);
         originBlock.innerHTML = content;
         let closeButton = document.createElement('div');
         closeButton.addEventListener('click', function(e) {
             document.querySelector('.hardware-price.choosed').classList.remove('choosed');
             getPrice()
             
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
             if (originBlock.querySelector('.hardware-close-div')) {
                originBlock.querySelector('.hardware-close-div').style.height = originBlock.offsetHeight + "px"; 
             }
             
         });
  
          
         let overlay = document.querySelector('.js-overlay-modal');
         modalElem = document.querySelector('.modal[data-modal="' + hardwareBlockClass + '"]');

         modalElem.classList.remove('active');
         overlay.classList.remove('active');
         getPrice()

      });
      

   });
    let btn = document.querySelector('.save-cfg-btn'),
      loader = document.querySelector('.loader'),
      img = document.querySelector('.check-img'),
      check = document.querySelector('.check');
  
      btn.addEventListener('click', function () {

        motherboard = document.querySelector('.origin-motherboard').querySelector('.hardware-name');
        if (!motherboard){
            setTimeout(removeCfgBtn, 6000);
            loader.classList.add('fail');
            check.classList.add('fail');
            loader.classList.add('active');
            return false;
        }
        
        cpu = document.querySelector('.origin-cpu').querySelector('.hardware-name');
          if (!cpu) {
              setTimeout(removeCfgBtn, 6000);
            loader.classList.add('fail');
            check.classList.add('fail');
            loader.classList.add('active');
              return false;
          }
        gpu = document.querySelector('.origin-gpu').querySelector('.hardware-name');
          if (!gpu) {
              setTimeout(removeCfgBtn, 6000);
            loader.classList.add('fail');
            check.classList.add('fail');
            loader.classList.add('active');
              return false;
          }
        ram = document.querySelector('.origin-ram').querySelector('.hardware-name');
          if (!ram) {
              setTimeout(removeCfgBtn, 6000);
            loader.classList.add('fail');
            check.classList.add('fail');
            loader.classList.add('active');
              return false;
          }
        ps = document.querySelector('.origin-ps').querySelector('.hardware-name');
          if (!ps) {
              setTimeout(removeCfgBtn, 6000);
            loader.classList.add('fail');
            check.classList.add('fail');
            loader.classList.add('active');
              return false;
          }
        pcCase = document.querySelector('.origin-case').querySelector('.hardware-name');
          if (!pcCase) {
              setTimeout(removeCfgBtn, 6000);
            loader.classList.add('fail');
            check.classList.add('fail');
            loader.classList.add('active');
              return false;
          }
        hdd = document.querySelector('.origin-hdd').querySelector('.hardware-name');
          if (!hdd) {
              setTimeout(removeCfgBtn, 6000);
            loader.classList.add('fail');
            check.classList.add('fail');
            loader.classList.add('active');
              return false;
          }
        let configurationName = document.getElementById("name").value;          
        let hardwareNames = {"motherboard":motherboard.textContent,
                             "cpu": cpu.textContent,
                             "gpu":gpu.textContent,
                             "ram":ram.textContent,
                             "ps":ps.textContent,
                             "drive":hdd.textContent,
                             "case":pcCase.textContent,
                             "name": configurationName}
          $.ajax({
              url : "/saveCfg",
              type : "POST",
              data : JSON.stringify(hardwareNames),
              contentType: 'application/json; charset=utf-8',
              dataType: 'json',

          })
        
        setTimeout(removeCfgBtn, 6000);
        loader.classList.add('active');
        img.style.display = 'none';
        
      });
      

      loader.addEventListener('animationend', function() {
        check.classList.add('active'); 
      });
    
    function removeCfgBtn() {
        loader.classList.remove('active');
        loader.classList.remove('fail');
        check.classList.remove('active');
        check.classList.remove('fail');
        img.style.display = 'block';
    };
    
    function getPrice() {
        priceList = document.querySelectorAll('.hardware-price.choosed');
          let rawDataToSend = []
          for (let i = 0; i < priceList.length; i++) {
              rawDataToSend.push(priceList[i].textContent);
          }
          let dataToSend = {'priceList': rawDataToSend};
          console.log(JSON.stringify(dataToSend));
          $.ajax({
                type: "POST",
                url: "/getprice",
                data: JSON.stringify(dataToSend),
                dataType: "json",
                contentType: 'application/json; charset=utf-8',
                dataType: 'json',
                success: function(result) {
                    document.querySelector('.final-price').innerHTML = '<h5>Итоговая цена: ' + result['price'] + ' руб.</h5>';
                }   
            });
    };
    
});