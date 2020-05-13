$(document).ready(function() {
    $('#search-btn-videogame').on('click', function(e) {
       e.preventDefault();
       var searchText = $('#search-box-videogame').val();
       $.ajax( {
           url: '/videogames/?search_filter=' + searchText,
           type: 'GET',
           success: function (resp) {
               var newHtml = resp.data.map(d => {
                   return `<div class="single-product">
                               <a href="/videogames/${d.id}">
                                   <img class="product-img" src="${d.image}" />
                                   <p class="product-name">${d.name}</p>
                               </a>
                            </div>`
               });
               $('.product').html(newHtml.join(''));
               $('#search-box-videogame').val('');
           },
           error: function (xhr, status, error) {
               console.error(error);
           }
       })
    });
});