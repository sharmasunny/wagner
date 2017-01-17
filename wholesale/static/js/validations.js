var checked_list=[];
(function($) {
	// Options for Message
	//----------------------------------------------
  var options = {
	  'btn-loading': '<i class="fa fa-spinner fa-pulse"></i>',
	  'btn-success': '<i class="fa fa-check"></i>',
	  'btn-error': '<i class="fa fa-remove"></i>',
	  'msg-success': 'All Good! Redirecting...',
	  'msg-error': 'Wrong login credentials!',
	  'useAJAX': true,
  };

	// Login Form
	//----------------------------------------------
	// Validation
  $("#login-form").validate({
  	rules: {
      id_username: "required",
  	  id_password: "required",
    },
  	errorClass: "form-invalid"
  });
  
	// Form Submission
  $("#login-form").submit(function() {
  	remove_loading($(this));
		
		if(options['useAJAX'] == true)
		{
			// Dummy AJAX request (Replace this with your AJAX code)
		  // If you don't want to use AJAX, remove this
  	  dummy_submit_form($(this));
		
		  // Cancel the normal submission.
		  // If you don't want to use AJAX, remove this
  	  return false;
		}
  });
	
	// Register Form
	//----------------------------------------------
	// Validation
  $("#register-form").validate({
  	rules: {
      reg_username: "required",
  	  reg_password: {
  			required: true,
  			minlength: 5
  		},
   		reg_password_confirm: {
  			required: true,
  			minlength: 5,
  			equalTo: "#register-form [name=reg_password]"
  		},
  		reg_email: {
  	    required: true,
  			email: true
  		},
  		reg_agree: "required",
    },
	  errorClass: "form-invalid",
	  errorPlacement: function( label, element ) {
	    if( element.attr( "type" ) === "checkbox" || element.attr( "type" ) === "radio" ) {
    		element.parent().append( label ); // this would append the label after all your checkboxes/labels (so the error-label will be the last element in <div class="controls"> )
	    }
			else {
  	  	label.insertAfter( element ); // standard behaviour
  	  }
    }
  });

  // Form Submission
  $("#register-form").submit(function() {
  	remove_loading($(this));
		
		if(options['useAJAX'] == true)
		{
			// Dummy AJAX request (Replace this with your AJAX code)
		  // If you don't want to use AJAX, remove this
  	  dummy_submit_form($(this));
		
		  // Cancel the normal submission.
		  // If you don't want to use AJAX, remove this
  	  return false;
		}
  });

	// Forgot Password Form
	//----------------------------------------------
	// Validation
  $("#forgot-password-form").validate({
  	rules: {
      fp_email: "required",
    },
  	errorClass: "form-invalid"
  });
  
	// Form Submission
  $("#forgot-password-form").submit(function() {
  	remove_loading($(this));
		
		if(options['useAJAX'] == true)
		{
			// Dummy AJAX request (Replace this with your AJAX code)
		  // If you don't want to use AJAX, remove this
  	  dummy_submit_form($(this));
		
		  // Cancel the normal submission.
		  // If you don't want to use AJAX, remove this
  	  return false;
		}
  });

	// Loading
	//----------------------------------------------
  function remove_loading($form)
  {
  	$form.find('[type=submit]').removeClass('error success');
  	$form.find('.login-form-main-message').removeClass('show error success').html('');
  }

  function form_loading($form)
  {
    $form.find('[type=submit]').addClass('clicked').html(options['btn-loading']);
  }
  
  function form_success($form)
  {
	  $form.find('[type=submit]').addClass('success').html(options['btn-success']);
	  $form.find('.login-form-main-message').addClass('show success').html(options['msg-success']);
  }

  function form_failed($form)
  {
  	$form.find('[type=submit]').addClass('error').html(options['btn-error']);
  	$form.find('.login-form-main-message').addClass('show error').html(options['msg-error']);
  }

	// Dummy Submit Form (Remove this)
	//----------------------------------------------
	// This is just a dummy form submission. You should use your AJAX function or remove this function if you are not using AJAX.
  function dummy_submit_form($form)
  {
  	if($form.valid())
  	{
  		form_loading($form);
  		
  		setTimeout(function() {
  			form_success($form);
  		}, 2000);
  	}
  }

  $(document).ready(function () {
    if(window.location.href.indexOf("logout") > -1) {
       setTimeout(
    function() {
      window.location.href='/'
    }, 3000);
    }
});

  
  /********************Get products for a category***********************/
  $('.category_name').click(function(){
    getcategory($(this).attr("data-id"));
  });

  getcategory(1);

function getcategory(catid){
    var category_id= catid;
      var params={'category_id':category_id}
      $.ajax({
          type : 'POST',
          url : '/get_products/',
          data : params,

          success:function(res){
            $('.thumbnail').html(res);


            $('.my-cart-btn').myCart({
              classCartIcon: 'my-cart-icon',
              classCartBadge: 'my-cart-badge',
              classProductQuantity: 'my-product-quantity',
              classProductRemove: 'my-product-remove',
              classCheckoutCart: 'my-cart-checkout',
              affixCartIcon: true,
              showCheckoutModal: true,
              cartItems: checked_list,
              clickOnAddToCart: function($addTocart){
                goToCartIcon($addTocart);
              },
              clickOnCartIcon: function($cartIcon, products, totalPrice, totalQuantity) {
                //console.log("cart icon clicked", $cartIcon, products, totalPrice, totalQuantity);
              },
              checkoutCart: function(products, totalPrice, totalQuantity) {
               console.log('dsdsa',products,totalPrice)
               var order_data = JSON.stringify(products);
                var total_price=totalPrice
                var params={'order_data':order_data,'total_price':total_price}
                $.ajax({
                    type : 'POST',
                    url : '/save_order/',
                    data : params,

                    success:function(res){
                     if(res=='success'){
                        $("#success_msg").show().delay(5000).fadeOut();
                      }
                    }
                });
              },
              getDiscountPrice: function(products, totalPrice, totalQuantity) {
                //console.log("calculating discount", products, totalPrice, totalQuantity);
                return totalPrice * 0.5;
              }
            });



             var goToCartIcon = function($addTocartBtn){    
              var checked_dict={};
              var id= parseFloat($addTocartBtn.attr('data-id'))
              checked_dict.id = parseFloat($addTocartBtn.attr('data-id'));
              checked_dict.price = parseFloat($addTocartBtn.attr('data-price'));
              checked_dict.name = $addTocartBtn.attr('data-name');
              checked_dict.quantity = parseInt($('#quantity_'+id).val());
              var check = true;
              checked_list.forEach(function(element,index) {
                if(element.id==id){
                  check = false;
                  element.quantity += checked_dict.quantity;
                }
              });

              if(check){
                checked_list.push(checked_dict);
              }  

              
              console.log(checked_list);

            }


          }

      })
  }

  /********************View Order**********************/
  $('.view_order').click(function(){
      var order_id=$(this).attr('data-id');
      var params={'order_id':order_id}
        $.ajax({
            type : 'POST',
            url : '/order_info/'+order_id+'/',
            data : params,

            success:function(res){
              window.location.href='/order_info/'+order_id+'/'
            }

      })
  }); 

  /***************Delete an order******************/
	$('.delete_order').click(function(){
      var order_id=$(this).attr('data-id');
      var params={'order_id':order_id}
        $.ajax({
            type : 'POST',
            url : '/delete_order/',
            data : params,

            success:function(res){
              if(res=='success'){
                window.location.reload();
              }
            }

      })
  }); 


/****************** Tabs to show edit user info and change password ******************************/
  $('#user_info').click(function(){
      $('#change_user_password').hide();
      $('#edit_user_profile').show();
  });
  $('#edit_password').click(function(){
      $('#edit_user_profile').hide();
      $('#change_user_password').show();
  });


  /***********************Edit User Info*************************/
   $('#contact_name').bind('keyup blur', function(){
        $(this).val( $(this).val().replace(/[^a-zA-Z\s]/g,'') );
    });
   $('#business_name').bind('keyup blur', function(){
        $(this).val( $(this).val().replace(/[^a-zA-Z\s]/g,'') );
    });
   $('#first_name').bind('keyup blur', function(){
        $(this).val( $(this).val().replace(/[^a-zA-Z\s]/g,'') );
    });
   $('#last_name').bind('keyup blur', function(){
        $(this).val( $(this).val().replace(/[^a-zA-Z\s]/g,'') );
    });
   $('#phone_number').bind('keyup blur', function(){
        $(this).val( $(this).val().replace(/[^0-9]/g,'') );
    });
   $('#fax').bind('keyup blur', function(){
        $(this).val( $(this).val().replace(/[^0-9]/g,'') );
    });
   $('#town').bind('keyup blur', function(){
        $(this).val( $(this).val().replace(/[^a-zA-Z\s]/g,'') );
    });
   $('#post_code').bind('keyup blur', function(){
        $(this).val( $(this).val().replace(/[^0-9]/g,'') );
    });
  $('#edit_user_info').click(function(){
      $('#save_info_changes').show();
      $("#username").removeAttr("disabled");
      $("#contact_name").removeAttr("disabled");
      $("#business_name").removeAttr("disabled");
      $("#delivery_instructions").removeAttr("disabled");
      $("#email").removeAttr("disabled");
      $("#first_name").removeAttr("disabled");
      $("#last_name").removeAttr("disabled");
      $("#phone_number").removeAttr("disabled");
      $("#fax").removeAttr("disabled");
      $("#address").removeAttr("disabled");
      $("#town").removeAttr("disabled");
      $("#post_code").removeAttr("disabled");
  });
      //Get fields values//
      var username = ''
      var contact_name = ''
      var business_name = ''
      var delivery_instructions = ''
      var email=''
      var first_name=''
      var last_name=''
      var phone_number = ''
      var fax = ''
      var address = ''
      var town = ''
      var post_code = ''
      username = $('#username').val();
      contact_name = $('#contact_name').val();
      business_name = $('#business_name').val();
      delivery_instructions = $('#delivery_instructions').val();
      email = $('#email').val();
      first_name = $('#first_name').val();
      last_name = $('#last_name').val();
      phone_number = $('#phone_number').val();
      fax = $('#fax').val();
      address = $('#address').val();
      town = $('#town').val();
      post_code = $('#post_code').val();


      //Get changed values
      $( "#username" ).change(function() {
        username = $('#username').val();
      });
      $( "#contact_name" ).change(function() {
        contact_name = $('#contact_name').val();
      });
      $( "#business_name" ).change(function() {
        business_name = $('#business_name').val();
      });
      $( "#delivery_instructions" ).change(function() {
        delivery_instructions = $('#delivery_instructions').val();
      });
      $( "#email" ).blur(function() {
        email = $('#email').val();
        var result=validateEmail(email);
        if(result == false){
          $("#invalid_email").show().delay(3000).fadeOut();
        }
        else{
            console.log('true')
        }
      });
      $( "#first_name" ).change(function() {
        first_name = $('#first_name').val();
      });
      $( "#last_name" ).change(function() {
        last_name = $('#last_name').val();
      });
      $( "#phone_number" ).change(function() {
        phone_number = $('#phone_number').val();
      });
      $( "#fax" ).change(function() {
        fax = $('#fax').val();
      });
      $( "#address" ).change(function() {
        address = $('#address').val();
      });
      $( "#town" ).change(function() {
        town = $('#town').val();
      });
      $( "#post_code" ).change(function() {
        post_code = $('#post_code').val();
      });
      var user_id = $('#user_id').val();
      //Saving to database//
      $('#save_info_changes').click(function(){
        console.log('info>>',username,contact_name,business_name,delivery_instructions,
                    email,first_name,last_name,phone_number,fax,town,post_code,address)
        if (user_id == '' || username == '' || contact_name == '' || business_name == '' || delivery_instructions == '' || email == '' ||
            first_name == '' || last_name == '' || phone_number == '' || fax == '' || town == '' || post_code == '' ||
            address == '') {
            $(".user_form :input").each(function() {
                if ($.trim($(this).val()) == "")
                  $(this).addClass("empty_field_class");
                  $(".empty_field_class").css({"border":"solid red 1px"});
            });
            $(".empty_error").show();
        }
        else{
          var params={'user_id':user_id,'username':username,'contact_name':contact_name,'business_name':business_name,'delivery_instructions':delivery_instructions,
                    'email':email,'first_name':first_name,'last_name':last_name,'phone_number':phone_number,'fax':fax,'address':address,
                    'town':town,'post_code':post_code}
          $.ajax({
              type : 'POST',
              url : '/edit_profile/',
              data : params,

              success:function(res){
                if (res == 'success') {
                  $(".successfull").show().delay(5000).fadeOut();
                  $('#save_info_changes').hide();
                  $("#username").attr("disabled", true);
                  $("#contact_name").attr("disabled", true);
                  $("#business_name").attr("disabled", true);
                  $("#delivery_instructions").attr("disabled", true);
                  $("#email").attr("disabled", true);
                  $("#first_name").attr("disabled", true);
                  $("#last_name").attr("disabled", true);
                  $("#phone_number").attr("disabled", true);
                  $("#fax").attr("disabled", true);
                  $("#address").attr("disabled", true);
                  $("#town").attr("disabled", true);
                  $("#post_code").attr("disabled", true);
                }
                else{
                  if (res == 'duplicate_email') {
                    $(".duplicate_email").show();
                  }
                  else{
                    $(".duplicate_username").show();
                  }
                  
                }
              }

          })
        }
        $(document).on('click', '.hide_error', function(){
          $(".error_field").hide();
        })
      })
      
      
      

   

/************************ Change password Functionality **************************/
      var user_email=''
      var old_password=''
      var new_password=''
      var confirm_password=''
      var changed_password=''

      //Get fields values//
      user_email = $('#user_email').val();
      old_password = $('#old_password').val();
      new_password = $('#new_password').val();
      confirm_password = $('#confirm_password').val();

      $( "#old_password" ).change(function() {
        old_password = $('#old_password').val();
      });
      $( "#new_password" ).change(function() {
        new_password = $('#new_password').val();
      });
      $( "#confirm_password" ).change(function() {
        confirm_password = $('#confirm_password').val();
        if (new_password == confirm_password) {
          changed_password = confirm_password

          $('#change_password').click(function(){
          if (user_email == '' || old_password == '' || changed_password == '') {
                $(".change_pass_form :input").each(function() {
                    if ($.trim($(this).val()) == "")
                      $(this).addClass("empty_field_class");
                      $(".empty_field_class").css({"border":"solid red 1px"});
                });
                $(".empty_error").show();
            }
            else{
              var params={'user_email':user_email,'old_password':old_password,'changed_password':changed_password}
              $.ajax({
                  type : 'POST',
                  url : '/change_password/',
                  data : params,

                  success:function(res){
                    if (res == 'success') {
                      $(".password_updated").show().delay(5000).fadeOut();
                    }
                    else{
                      $(".password_failed").show().delay(5000).fadeOut();
                    }
                  }

              })
            }
            
          })

        }
        else{
          $("#password_mismatch").show().delay(3000).fadeOut();
        }

      });
      
    
    $(document).on('click', '.hide_error', function(){
      $(".error_field").hide();
    })

  /**********************Function to validate an email*************************/
  function validateEmail(email) {
    var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
}
})(jQuery);