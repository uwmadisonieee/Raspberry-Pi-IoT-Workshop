function buttonClick(button) {
	if (button == 0) {
		$.get("/LED/0", function() {
			console.log("Turned LED off");
		});
	} else if (button == 1) {
		$.get("/LED/1", function() {
			console.log("Turned LED on");
		});
	} else if (button == 2) {

	} else if (button == 3) {

	}
}