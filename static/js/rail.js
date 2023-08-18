$(document).ready(function(){
    $(".step-down-btn").click(function(){
      const n_input = $("input[name='number-setting']")[0]
      let c_v = parseInt(n_input.value);
      n_input.value = c_v - 1;
  
    });
    $(".step-up-btn").click(function(){
      const n_input = $("input[name='number-setting']")[0]
      let c_v = parseInt(n_input.value);
      n_input.value = c_v + 1;
    });
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
      const key = $("input[name='number-setting']").val();
      const type = $(".process-btn").text().toLowerCase();
      const text = $("#plaintext-area").val();
      let dat = {"type": type, "key": key, "text": text};
      $.ajax({
          url: "/api/rail/",
          type: "POST",
          contentType: "application/json",
          data: JSON.stringify(dat),
          success: function(result) {
            $("#ciphertext-area").val(result.output);
          }
      });
    });
  });