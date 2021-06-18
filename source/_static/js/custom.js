document.addEventListener("DOMContentLoaded", function () {
  addLinkToPyPI();
  addLinkToGitHub();
  handlePreviewWindow();
  addTargetToExternalReferences();
  handlePreviewGallery();
});

function addLinkToPyPI() {
  const versionElem = document.querySelector("#navbar .navbar-version b");
  const versionParentElem = versionElem.parentElement;
  const linkElem = document.createElement("a");
  linkElem.href = "https://pypi.org/project/lets-plot";
  linkElem.classList.add("reference", "external");
  linkElem.appendChild(versionElem);
  versionParentElem.appendChild(linkElem);
}

function addLinkToGitHub() {
  const logoSize = document.getElementsByClassName('navbar-version')[0].clientHeight;
  const logoElem = document.createElement("div");
  logoElem.classList.add("github-logo");
  logoElem.style.display = "block";
  logoElem.style.width = logoSize + "px";
  logoElem.style.height = logoSize + "px";
  const linkElem = document.createElement("a");
  linkElem.href = "https://github.com/JetBrains/lets-plot";
  linkElem.classList.add("navbar-brand", "reference", "external");
  linkElem.appendChild(logoElem);
  document.querySelector("#navbar .navbar-header").appendChild(linkElem);
}

function handlePreviewWindow() {
  const previewPickerLinkElems = document.getElementsByClassName('preview-picker')[0].getElementsByClassName('reference');
  const previewWindowLinkElem = document.getElementsByClassName('preview-window')[0].getElementsByClassName('reference')[0];
  const previewWindowImageElem = previewWindowLinkElem.getElementsByTagName('img')[0];
  const previewLinkOnClick = function (event) {
    event.preventDefault();
    previewWindowImageElem.setAttribute('src', event.target.getAttribute('src').replace('200x200', '1024x768'));
    previewWindowLinkElem.setAttribute('href', event.currentTarget.getAttribute('href'));
  }

  for (let i = 0; i < previewPickerLinkElems.length; i++)
    previewPickerLinkElems[i].onclick = previewLinkOnClick;
}

function addTargetToExternalReferences() {
  const links = document.getElementsByClassName('reference external');
  for (let i = 0; i < links.length; i++)
    links[i].setAttribute('target', '_blank');
}

function handlePreviewGallery() {
  const previewsPerRow = 4;
  const previews = document.getElementsByClassName('preview-gallery')[0].getElementsByClassName('d-flex');
  const updatePreviewGallery = function (currentHiddenRowId) {
    for (let i = 0; i < previews.length; i++)
      if (i < currentHiddenRowId * previewsPerRow)
        previews[i].classList.remove('hidden');
      else
        previews[i].classList.add('hidden');
  }
  let hiddenRowId = 1;
  const loadMoreOnClick = function (event) {
    event.preventDefault();
    hiddenRowId++;
    updatePreviewGallery(hiddenRowId);
  }
  updatePreviewGallery(hiddenRowId);
  document.getElementById('preview-gallery-more').getElementsByTagName('a')[0].onclick = loadMoreOnClick;
}