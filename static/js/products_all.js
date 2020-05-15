$(document).ready(function() {
    $('#search-btn-all').on('click', function(e) {
       e.preventDefault();
       var searchText = $('#search-box-all').val();
       $.ajax( {
           url: '/products/?search_filter=' + searchText,
           type: 'GET',
           success: function (resp) {
               var newHtml = resp.data.map(d => {
                   if  (d.type_id == 1) {
                       return `<div class="single-product">
                               <a href="/consoles/${d.id}">
                                   <img class="product-img" src="${d.image}" />
                                   <p class="product-name">${d.name}</p>
                                   <p class="prodict-price">${d.price}</p>
                               </a>
                            </div>`
                   }
                   else if  (d.type_id == 2) {
                       return `<div class="single-product">
                               <a href="/videogames/${d.id}">
                                   <img class="product-img" src="${d.image}" />
                                   <p class="product-name">${d.name}</p>
                                   <p class="prodict-price">${d.price}</p>
                               </a>
                            </div>`
                   }
                   else if  (d.type_id == 3) {
                       return `<div class="single-product">
                               <a href="/accessories/${d.id}">
                                   <img class="product-img" src="${d.image}" />
                                   <p class="product-name">${d.name}</p>
                                   <p class="prodict-price">${d.price}</p>
                               </a>
                            </div>`
                   }
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