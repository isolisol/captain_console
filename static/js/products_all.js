$(document).ready(function() {
    $('#search-btn-all').on('click', function(e) {
       e.preventDefault();
       var searchText = $('#search-box-all').val();
       $.ajax( {
           url: '/products/?search_filter=' + searchText,
           type: 'GET',
           success: function (resp) {
               var newHtml = resp.data.map(d => {
                   return `<div class="single-product">
                               <a href="/products/${d.id}">
                                   <img class="product-img" src="${d.image}" />
                                   <p class="product-name">${d.name}</p>
                                   <p class="prodict-price">${d.price}</p>
                               </a>
                            </div>`
               });
               $('.product').html(newHtml.join(''));
               $('#search-box-all').val('');
           },
           error: function (xhr, status, error) {
               console.error(error);
           }
       })
    });
});