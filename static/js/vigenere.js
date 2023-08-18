$(document).ready(function(){
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
    $(".process-btn").click(function() {
      const text = $("#plaintext-area").val();
      const key = $("input[name='text-key']").val();
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
          for (let i = 0; i < key.length; i++) {
            kunci = key.charCodeAt(i);
            if ((kunci < 65 || (kunci > 90 && kunci < 97) && kunci > 122) && kunci!=32) {
                $.bootstrapGrowl("Kunci harus berupa karakter!!", {
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
                for (let j = 0; j < key.length; j++) {
                  kunci = key.charCodeAt(j);
                  if ((kunci > 64 && kunci < 91) || (kunci > 96 && kunci < 123) || kunci == 32){
                    const type = $(".process-btn").text().toLowerCase();
                    let data = {"type": type, "key": key, "text": text};
                    $.ajax({
                      url: "/api/vigenere/",
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