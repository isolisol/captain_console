$(document).ready(function() {
    $('#search-btn-accessory').on('click', function(e) {
       e.preventDefault();
       var searchText = $('#search-box-accessory').val();
       $.ajax( {
           url: '/accessories/?search_filter=' + searchText,
           type: 'GET',
           success: function (resp) {
               var newHtml = resp.data.map(d => {
                   return `<div class="single-product">
                               <a href="/accessories/${d.id}">
                                   <img class="product-img" src="${d.image}" />
                                   <p class="product-name">${d.name}</p>
                                   <p class="prodict-price">${d.price}</p>
                               </a>
                            </div>`
               });
               $('.product').html(newHtml.join(''));
               $('#search-box-accessory').val('');
           },
           error: function (xhr, status, error) {
               console.error(error);
           }
       })
    });
});