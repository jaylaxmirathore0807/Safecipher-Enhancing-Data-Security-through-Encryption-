$(document).ready(function(){
    $(".step-down-btn1").click(function(){
        const n_input = $("input[name='number-setting-caesar']")[0]
        let c_v = parseInt(n_input.value);
        n_input.value = c_v - 1;
    
      });
      $(".step-up-btn1").click(function(){
        const n_input = $("input[name='number-setting-caesar']")[0]
        let c_v = parseInt(n_input.value);
        n_input.value = c_v + 1;
      });
      $(".step-down-btn2").click(function(){
        const n_input = $("input[name='number-setting-rail']")[0]
        let c_v = parseInt(n_input.value);
        n_input.value = c_v - 1;
    
      });
      $(".step-up-btn2").click(function(){
        const n_input = $("input[name='number-setting-rail']")[0]
        let c_v = parseInt(n_input.value);
        n_input.value = c_v + 1;
      });
    $("input[name='text-key']").val();
    $(".action-encode").click(function () {
      $(".action-encode").toggleClass("mid-box-action-active");
      $(".action-decode").toggleClass("mid-box-action-active");
      $(".process-btn").text("Encrypt");
      $("#plaintext-area").val("");
      $("#ciphertext-area").val("");
      $(".box-title-right").text("Ciphertext");
      $(".box-title-left").text("Plaintext");
    });
    $(".action-decode").click(function () {
      $(".action-decode").toggleClass("mid-box-action-active");
      $(".action-encode").toggleClass("mid-box-action-active");
      $(".process-btn").text("Decrypt");
      $("#plaintext-area").val("");
      $("#ciphertext-area").val("");
      $(".box-title-right").text("Plaintext");
      $(".box-title-left").text("Ciphertext");
    });
    $(".process-btn").click(function () {
      const key1 = $("input[name='number-setting-caesar']").val();
      const key2 = $("input[name='number-setting-rail']").val();
      const key3 = $("input[name='text-key']").val();
      const text = $("#plaintext-area").val();
      for (let i = 0; i < text.length; i++) { 
        teks = text.charCodeAt(i);
        if ((teks < 65 || (teks > 90 && teks < 97) || teks > 122) && teks !=32) {
            $.bootstrapGrowl("Masukkan harus berupa karakter!!", {
              ele: 'body', // which element to append to
              type: 'danger', // (null, 'info', 'danger', 'success')
              offset: {from: 'top', amount: 400}, // 'top', or 'bottom'
              align: 'center', // ('left', 'right', or 'center')
              width: 350, // (integer, or 'auto')
              delay: 1500, // Time while the message will be displayed. It's not equivalent to the *demo* timeOut!
              allow_dismiss: true, // If true then will display a cross to close the popup.
              stackup_spacing: 10, // spacing between consecutively stacked growls.
            });
          $(".process-btn").preventDefault();
        }
      }
      for (let i = 0; i < key3.length; i++) {
        kunci = key3.charCodeAt(i);
        if ((kunci < 65 || (kunci > 90 && kunci < 97) && kunci > 122) && kunci!=32) {
            $.bootstrapGrowl("Kunci 3 harus berupa karakter!!", {
              ele: 'body', // which element to append to
              type: 'danger', // (null, 'info', 'danger', 'success')
              offset: {from: 'top', amount: 400}, // 'top', or 'bottom'
              align: 'center', // ('left', 'right', or 'center')
              width: 350, // (integer, or 'auto')
              delay: 1500, // Time while the message will be displayed. It's not equivalent to the *demo* timeOut!
              allow_dismiss: true, // If true then will display a cross to close the popup.
              stackup_spacing: 10, // spacing between consecutively stacked growls.
            });
            $(".process-btn").preventDefault();
        }
      }
      for (let i = 0; i < text.length; i++) {
        teks = text.charCodeAt(i);
        if ((teks > 64 && teks < 91) || (teks > 96 && teks < 123) || teks == 32) {
          for (let j = 0; j < key3.length; j++) {
            kunci = key3.charCodeAt(j);
            if ((kunci > 64 && kunci < 91) || (kunci > 96 && kunci < 123) || kunci == 32){
              const type = $(".process-btn").text().toLowerCase();
              let data = {"type": type, "key1": key1, "key2": key2, "key3": key3, "text": text};
              $.ajax({
                  url: "/api/super/",
                  type: "POST",
                  contentType: "application/json",
                  data: JSON.stringify(data),
                  success: function(result) {
                    $("#ciphertext-area").val(result.output);
                  }
              });
            }
          }
        }
      }
    });
  });