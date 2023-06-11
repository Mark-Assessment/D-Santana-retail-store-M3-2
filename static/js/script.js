$(document).ready(function(){
    $(".sidenav").sidenav();
    $('.collapsible').collapsible({
      accordion: false
    });
    $(document).ready(function(){
      $('.parallax').parallax();
    });  
    $('.tooltipped').tooltip();
    $('.collapsible').collapsible({
      accordion: false
    });
    $('select').formSelect();
    $('.datepicker').datepicker({
      format: "yyyy-mm-dd",
      yearRange: 3,
      showClearBtn: true,
      i18n: {
        done: "Select"
      }
    });
  });

  