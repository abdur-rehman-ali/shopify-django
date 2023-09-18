$('#slider1, #slider2, #slider3').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 5,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})
const BASE_URL = 'http://localhost:8000'

const updateCartAmount = (response) => {
    const {
        amount_without_shipping,
        amount_with_shipping,
        shipping,
    } = response
    $("#amount_without_shipping").text(`€ ${amount_without_shipping}`)
    $("#amount_with_shipping").text(`€ ${amount_with_shipping}`)
    $("#shipping").text(`€ ${shipping}`)
}

$('.plus-cart').click(function () {
    const actionButtons = $(this).closest("#action-buttons")
    const productID = actionButtons.find("#product-id").text()
    $.ajax({
        type: 'GET',
        url: `${BASE_URL}/update-cart`,
        data: {
            'product_id': productID
        },
        success: function (response) {
            const { quantity } = response
            actionButtons.find("#quantity").text(quantity)
            updateCartAmount(response)
        }
    })
})
