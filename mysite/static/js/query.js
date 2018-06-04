
$(document).ready(function(){



  // Greatest Common Divisor Well
  $("#gcd_button").click( function(event) {
    $.post("/calculator/gcd/",{"a": $("#gcd_a").val(),"b": $("#gcd_b").val()},(data,status) => {
      $("#gcd").val(data)
    })
  })

  // Prime Factorization well
  $("#prime_factorization_button").click( function(event) {
    $.post("/calculator/prime_factorization/",{"a": $("#prime_fact_a").val()},(data,status) => {
      $("#prime_factors").val(data)
    })
  })


})
