# Exchange_django-ajax_app

Modern verion of exchange_django_app.</br>
It works with simple POST ajax request.
```
$.ajax({
    type: 'POST',
    url: '{% url "post_index" %}',
    data: serializedData,

    success: function(response){
      console.log('total = ', response['total'])
        $('#total_h4').html(response['total']);
    },
    error: function(response){
        $('#total_h4').innerHTML = 'Oops, error!';
    },
})
```
