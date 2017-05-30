var client = algoliasearch('B6KQUPHS9M', 'bc54b1bf2df17f1a41dd23cae387af02');
var index = client.initIndex('recipes');
var rawFile = new XMLHttpRequest();
var query = getParam('q') || '';
var category = getParam('cat') || '*';
document.getElementById('search').value = query;
document.getElementById('sel').value = category;
if (query) {
    index.search(
        query,
        {facets: category},
        function searchDone(err, content) {
            if (err) {
                console.error(err);
                return;
            }

            document.getElementById('results').innerHTML = '';
            for (var h in content.hits) {
                rawFile.open('GET', content.hits[h].folder + '/' + content.hits[h].file, false);
                rawFile.send();
                document.getElementById('results').innerHTML +=
                '<li><h3><a href=" + content.hits[h].folder + "/"' + content.hits[h].file + '">' + content.hits[h]._highlightResult.friendlyName.value + '</a></h3><code class="prettyprint">' + rawFile.responseText + '</code></li>';
            }
            PR.prettyPrint();
        }
    );
} else {
    document.getElementById('results').innerHTML = '';
}

document.getElementById('search').onkeypress = _.debounce(function () {
    if (document.getElementById('search').value) {
        index.search(
            document.getElementById('search').value,
            {facets: document.getElementById('sel').value},
            function searchDone(err, content) {
                if (err) {
                    console.error(err);
                    return;
                }

                document.getElementById('results').innerHTML = '';
                for (var h in content.hits) {
                    rawFile.open('GET', content.hits[h].folder + '/' + content.hits[h].file, false);
                    rawFile.send();
                    document.getElementById('results').innerHTML +=
                    '<li><h3><a href=" + content.hits[h].folder + "/" + content.hits[h].file + ">' + content.hits[h]._highlightResult.friendlyName.value + '</a></h3><code class="prettyprint">' + rawFile.responseText + '</code></li>';
                }
                PR.prettyPrint();
            }
        );
    } else {
        document.getElementById('results').innerHTML = '';
    }
}, 1);

document.getElementById('search').onkeydown = function (event) {
    if (event.keyCode === 8) document.getElementById('search').onkeypress();
};
document.getElementById('sel').click = document.getElementById('search').onkeypress;

function getParam(name) {
    url = window.location.href;
    name = name.replace(/[\[\]]/g, '\\$&');
    var regex = new RegExp('[?&]' + name + '(=([^&#]*)|&|#|$)'),
        results = regex.exec(url);
        if (!results) return null;
        if (!results[2]) return '';
        return decodeURIComponent(results[2].replace(/\+/g, ' '));
}
