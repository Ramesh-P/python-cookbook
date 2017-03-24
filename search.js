var client = algoliasearch("B6KQUPHS9M", "bc54b1bf2df17f1a41dd23cae387af02");
var index = client.initIndex("recipes");
var rawFile = new XMLHttpRequest();

document.getElementById("search").onkeypress = function () {
    index.search(
        document.getElementById("search").value,
        function searchDone(err, content) {
            if (err) {
                console.error(err);
                return;
            }

            document.getElementById("results").innerHTML = "";
            for (var h in content.hits) {
                rawFile.open("GET", content.hits[h].folder + "/" + content.hits[h].file, false);
                rawFile.send();
                document.getElementById("results").innerHTML +=
                "<li><h3><a href='" + content.hits[h].folder + "/" + content.hits[h].file + "'>" + content.hits[h].friendlyName + "</a></h3><code class='prettyprint'>" + rawFile.responseText + "</code></li>";
            }
            PR.prettyPrint();
        }
    );
};

document.getElementById("search").onkeydown = function (event) {
    if (event.keycode === 8) document.getElementById("search").onkeypress();
};
