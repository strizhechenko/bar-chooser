x = new Vue({
    el: "#app",
    data: {
        OLEG_KEYS: ['Мясо', 'По вегану', 'Пивчара', 'Винишко', 'Коктейли', 'Музыка', 'Недорого', 'Возле работы', 'Возле дома', 'В центре'],
        EKB_BARS: {
            'Пан-сметан': [2, 1, 2, 1, 1, 0, 0, 0, 2, 0],
            'Янки-бар': [1, 1, 2, 0, 0, 1, 1, 0, 0, 1],
            'Jawsspot': [0, 0, 2, 0, 0, 1, 1, 0, 0, 1],
            'New bar': [1, 0, 1, 0, 1, 2, 1, 0, 0, 1],
            'Ratskeller': [2, 1, 2, 1, 1, 0, 0, 0, 0, 2],
            'Маруся': [0, 0, 1, 0, 0, 0, 2, 0, 0, 1],
            'Peperonni': [1, 1, 1, 1, 0, 0, 1, 0, 0, 1],
            'Мизантроп': [0, 0, 1, 0, 1, 2, 1, 0, 0, 1],
            '8500': [1, 1, 1, 1, 2, 0, 1, 2, 0, 0],
            'Языки': [1, 1, 2, 1, 1, 0, 1, 0, 0, 1],
            'Рататуй': [2, 2, 1, 2, 1, 0, 1, 1, 0, 0],
            'Телячьи нежности': [2, 1, 1, 1, 1, 0, 0, 1, 0, 0],
            'На работе': [0, 0, 2, 0, 0, 1, 1, 0, 1, 0]
        }
    }
})

function rate(expectations, ratings) {
    var rating = 0;
    for (var i = 0; i < expectations.length; i++) {
        rating += Math.min(ratings[i], expectations[i]);
    }
    return rating;
}

function get_expectations() {
    return Array.from(document.getElementsByName("expected_rating")).map(function (a) {
        return parseInt(a.value);
    })
}

function rate_all() {
    var expectations = get_expectations();
    for (var bar in x.$data['EKB_BARS']) {
        var ratings = x.$data['EKB_BARS'][bar];
        var row = document.getElementById(bar);
        var rating = row.children.namedItem("rating");
        rating.textContent = rate(expectations, ratings);
    }
}
