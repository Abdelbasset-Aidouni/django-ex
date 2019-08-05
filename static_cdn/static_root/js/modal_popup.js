      


  
  var costumModals  = $(".costum-modal");
  var chooseFileButton  = '<div><button class="btn btn-info d-inline" role="file-upload">Choisir un fichier</button><input role="filename-display" type="text" class="form-control-plaintext d-inline px-2 w-50" readonly value="aucun fichier choisi"></div>';
  $.each(costumModals,(key,value) => {
          $(value).find("input").not("input[type=file]").addClass("form-control");
          $(value).find("input[type=file]").addClass("d-none");
          $(value).find("input[type=file]").after(chooseFileButton);
    });

  $(".costum-modal").find("button[role=file-upload]").click(function (event) {
    let inputFile = $(this).parent().parent().find("input[type=file]");
    
    inputFile.click();
    console.log("raha tmchii");
    
  });
  $(".costum-modal").find("input[type=file]").on("change",function (event) {
    $(this).parent().find("input[role='filename-display']").val($(this).val().substr($(this).val().lastIndexOf("\\")+1));
  })

  
  
      
      $(".costum-modal").find("button[type=submit]").click(function (event) {
        event.preventDefault();
        let modalLink    = String(this.getAttribute("modal"));
        let modalElement = $("#" + String(this.getAttribute("modal")));
        let modalRole    = this.getAttribute("role");
        let spinner     = modalElement.parent().find(".costum-modal-spinner-container");
        var protocol    = location.protocol;
        var slashes     = protocol.concat("//");
        var host        = slashes.concat(window.location.hostname);
        let endPoint    = this.getAttribute("endpoint");
        let formData    = $(this.parentElement.parentElement.parentElement).serialize();
        host            += ":" + window.location.port;

        
          let inputSet    = modalElement.find("input");
          let fields      = {};
          $.each(inputSet,(key,value) => {
            fields[String($(value).attr("name"))] = $(value).val();
          });
          let form_is_valide = validateFields(fields);
        
        
        if ( form_is_valide != true) {
          setErrMessage(form_is_valide);
          openModal("confirmation-modal",null,"req-failed",true);
        }else{
        modalElement.css({"opacity":"0.8"});
        spinner.show();
        
        
        $.ajax(
          {
            url: host + endPoint, 
            method:"POST",
            data:formData,
            success: function(resulte){
                        console.log("mriiigla belmsak",resulte);
                        modalElement.css({"opacity":"1"});
                        spinner.hide();
                        closeModal(modalLink);
                        setSuccessMsg();
                        openModal("confirmation-modal",null,"req-success");
            },
            error:function (err) {
                        console.log("the err is ",err);
                        modalElement.css({"opacity":"1"});
                        spinner.hide();
                        closeModal(modalLink);
                        setErrMessage();
                        openModal("confirmation-modal",null,"req-failed");
            }
          });
        }
      
        
      
      });

      function appendInfoElements(element,data){
        let bodyElement = $(element).find(".costum-modal-body");
        
        $(bodyElement).html("");
        $(bodyElement).append('<div class="container"><div class="row"><div class="container content"></div></div></div>');
        
        bodyElement = $(bodyElement).find(".content");

        
        let content;
        let htmlContent;
        $.each(data, (key,value) =>{
          content = value["designation"];

          htmlContent = `<div class="row align-content-center requirement-container"><div class="pin d-inline-flex"></div><div class="requirement-content d-inline px-3">${content} </div></div>`;

          $(bodyElement).append(htmlContent);

        });
        
      }




      function getInfo(element){

            let modalLink    = String(element.getAttribute("modal"));
            let modalElement = $("#" + modalLink);
            
            
            let spinner     = modalElement.parent().find(".costum-modal-spinner-container");
            var protocol    = location.protocol;
            var slashes     = protocol.concat("//");
            var host        = slashes.concat(window.location.hostname);
            let endPoint    = element.getAttribute("endpoint");
            
            host            += ":" + window.location.port;
            
            spinner.show();
            console.log(spinner);
            $.ajax(
              {
                url: host + endPoint, 
                method:"GET",
                success: function(resulte){
                            
                            console.log("mriiigla belmsak",resulte);

                            appendInfoElements(modalElement,resulte);
                            
                            spinner.hide();
                            
                            
                            
                            
                            
                },
                error:function (err) {
                            console.log("the err is ",err);
                            modalElement.css({"opacity":"1"});
                            spinner.hide();
                            closeModal(modalLink);
                            
                            setErrMessage("une erreur inattendue s'est produite. veuillez réessayer ultérieurement");
                            openModal("confirmation-modal",null,"req-failed");
                }
              });
      }



      function getBodyEvent(event) {
        let modalLink   = $("body").attr('modal');
        let keyCode     = event.keyCode;
        if (keyCode == 27) closeModal(modalLink);
      }



      function getTriggeredElement(element,event){
        let x     = event.target.className;
        if ( x.search("modal-in-the-show")>0 )  
          {
           closeModal(element.firstElementChild.id); 
          }
      }




      $(".modal-trigger").click(function (){
          let modalRole = this.getAttribute("role");
          let modalLink = this.getAttribute("modal");
          let endPoint  = this.getAttribute("endpoint");
          if (modalRole == "info")  getInfo(this);
          if (endPoint) openModal(modalLink,endPoint)
          else openModal(modalLink);
          
          
      });


      $(".modal-dismiss").click(function (event){
          event.preventDefault();
          let modalLink = this.getAttribute("modal");
          closeModal(modalLink);
      });


      function openModal(modalLink,endpoint=null,className=null,nested=false) {
        let modalElement    = $("#" + String(modalLink));
        let modalContainer  = modalElement.parent();

        if (className) modalElement.attr("class",className + " costum-modal container col-10 col-sm-8 col-md-5");
        modalContainer.fadeIn(300);
        if (endpoint) modalElement.find("button[type=submit]").attr("endpoint",endpoint);
        modalElement.fadeIn("slow");
        modalContainer.toggleClass("modal-in-the-show");
        if (!nested) {
          $("body").attr('onkeydown','getBodyEvent(event);');
        }else{
          modalContainer.css({"z-index":"10000"});
          modalElement.css({"z-index":"20000"});
          modalElement.attr("parent-modal",$("body").attr('modal'));
        }
        $("body").attr('modal',String(modalLink));
        
      }


      function closeModal(modalLink) {
        let modalElement    = $("#" + String(modalLink));
        let modalContainer  = modalElement.parent();
        let parentModal     = modalElement.attr("parent-modal");
        if (parentModal){
          $("body").attr('modal',String(parentModal));
        }else{
          $("body").removeAttr('onkeydown');
          $("body").removeAttr('modal');
        }

        modalElement.fadeOut(300);
        modalContainer.fadeOut(250);
          setTimeout(
            function() 
            {
              modalContainer.toggleClass("modal-in-the-show");
            }, 310);
        modalElement.css("display","none");
      }



      function phoneNumberValidator(field){
        if (String(field)[0] != 0) return false;
        if (typeof parseInt(field) != "number")  return false;
        console.log("field is a number");
        if (field.toString().length != 10 ) return false;
        
        return true;
      }

      function validateFields(fields){
        if (!phoneNumberValidator(fields["phone_number"])) return "svp entrer un numéro de telephone valide";
        return true;
      }

      function setErrMessage(msg=null){
        if (!msg) msg = "une erreur inattendue s'est produite. veuillez vérifier la conformité de vos informations réessayer ultérieurement";
        $("#confirmation-modal").find(".costum-modal-body").html(msg);
      }

      function setSuccessMsg(msg=null){
        if (!msg) msg = "Merci pour votre soumission vous sera contacté ultérieurement ";
        $("#confirmation-modal").find(".costum-modal-body").html(msg);
      }

      



      