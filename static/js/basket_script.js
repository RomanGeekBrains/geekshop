jQuery(document).ready(function () {

    /*
    // можем получить DOM-объект меню через JS
    var menu = document.getElementsByClassName('menu')[0];
    menu.addEventListener('click', function () {
        console.log(event);
        event.preventDefault();
    });
    
    // можем получить DOM-объект меню через jQuery
    $('.menu').on('click', 'a', function () {
        console.log('event', event);
        console.log('this', this);
        console.log('event.target', event.target);
        event.preventDefault();
    });
   
    // получаем атрибут href
    $('.menu').on('click', 'a', function () {
        var target_href = event.target.href;
        if (target_href) {
            console.log('нужно перейти: ', target_href);
        }
        event.preventDefault();
    });
    */

    // добавляем ajax-обработчик для обновления количества товара
    $('.basket_list').on('click', 'input[type="number"]', function () {
        let target_href = event.target;
        if (target_href) {
            $.ajax({
                url: "/basket/edit/" + target_href.name + "/" + target_href.value + "/",
                success: function (data) {
                    console.log(data);
                    $('.basket_summary').html(`В корзине ${data['total_quantity']} товаров общей стоимостью ${data['total_cost']} руб`);
                    //эксперемнты и записки 
                    // for (let key in data){
                    //     console.log(key);
                    //     console.log(data[key])
                    // }
                    // var l = Object.keys(data).length
                    // for(;l > 0; l--){
                    //     console.log(l);
                    //     console.log(data[1])
                    // }
                    // $('.product_cost').html(`Всего ${data['Basket object (30)']}&nbspруб за {{ item.product_quantity }} шт`)
                    console.log('ajax done');
                },
            });
        }
        event.preventDefault();
    });
});