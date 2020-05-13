$(document).ready(function() {
    $('#search-btn-console').on('click', function(e) {
       e.preventDefault();
       var searchText = $('#search-box-console').val();
       $.ajax( {
           url: '/consoles/?search_filter=' + searchText,
           type: 'GET',
           success: function (resp) {
               var newHtml = resp.data.map(d => {
                   return `<div class="single-product">
                               <a href="/consoles/${d.id}">
                                   <img class="product-img" src="${d.image}" />
                                   <p class="product-name">${d.name}</p>
                               </a>
                            </div>`
               });
               $('.product').html(newHtml.join(''));
               $('#search-box-console').val('');
           },
           error: function (xhr, status, error) {
               console.error(error);
           }
       })
    });
});