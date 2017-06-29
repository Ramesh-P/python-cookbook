var client = algoliasearch('B6KQUPHS9M', 'bc54b1bf2df17f1a41dd23cae387af02');
var index = client.initIndex('recipes');
var rawFile = new XMLHttpRequest();
var query = document.getElementById('query');
var cat = document.getElementById('cat');

query.addEventListener('input', search);
cat.addEventListener('change', search);
search();

function search() {
  if (query) {
    index.search(
      query.value,
      {filters: cat.value === '*' ? '' : 'folder:' + cat.value},
      function searchDone(err, content) {
        if (err) {
          console.error(err);
          return;
        }
        if (content.hits.length === 0) {
          document.getElementById('root').innerHTML = '<p align="middle"><big>Your search has returned no results.<big></p>';
        } else {
          document.getElementById('root').innerHTML = '';
          for (var h in content.hits) {
            rawFile.open(
              'GET', content.hits[h].folder + '/' + content.hits[h].file,
              false
            );
            rawFile.send();
            document.getElementById('root').innerHTML +=
              '<li class="list-group-item"><a download href="' +
              content.hits[h].folder +
              '/' +
              content.hits[h].file +
              '"><button type="button" class="btn btn-primary pull-right"><i class="fa fa-cloud-download" aria-hidden="true"></i></span> Download</button></a><h3>' +
              content.hits[h]._highlightResult.friendlyName.value +
              '</h3><pre class="prettyprint"><code>' +
              rawFile.responseText + '</code></pre></li>';
          }
          PR.prettyPrint();
        }
      }
    );
  }
}
