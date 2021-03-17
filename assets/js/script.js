function readCookie(name, document) {
    return parseInt(document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)')?.pop() || '0')
}

function autorefresh(templates, div_id, doc) {
    $.ajax({
        url: templates,
        success: function (data) {
            $(div_id).html($(div_id, data));
        },
    });
    window.scrollTo(readCookie('Txpos', doc), readCookie('Typos', doc));
}
