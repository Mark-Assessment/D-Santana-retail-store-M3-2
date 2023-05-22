$(document).ready(function(){
    $(".sidenav").sidenav();
    $('.collapsible').collapsible({
      accordion: false
    });
    $('.tooltipped').tooltip();
    $('.collapsible').collapsible({
      accordion: false
    });
    $('.datepicker').datepicker({
      format: "data mmm, yyyy",
      yearRange: 3,
      showClearBtn: true,
      i18n: {
        done: "Select"
      }
    });
  });

  