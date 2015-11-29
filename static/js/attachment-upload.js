(function(_) {
"use strict";

// http://stackoverflow.com/questions/14069421/show-an-image-preview-before-upload
// http://www.sitepoint.com/html5-javascript-file-upload-progress-bar/
// https://developer.mozilla.org/en-US/docs/Using_files_from_web_applications

var createUploader = function(element) {
	_.addClass(uploadElement, 'element');
};


var register = function(root) {
	if (!_.checkFeatures(["ajax", "drop", "file"])) {
		return;
	}

	_.forEach(_.cls(root, 'attachment-upload'), function(uploadElement) {
		createUploader(uploadElement);
	});
};

_.onLoad(function(e) { register(e.memo); });

}(_utils));