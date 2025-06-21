#include <iostream>
#include <string>
using namespace std;

// Success and Error codes
const char* s = "[+]";
const char* f = "[-]";
const char* c = "[*]";

// This function passes length, width and height arguments to main()
void multiply(int len, int wid, int hei) {
	int area = len * wid * hei; // Once integers are passed, they are then multiplied
	cout << "%s Length passed through from main: " << len << "\n", c;
	cout << "Width passed through from main: " << wid << "\n", c;
	cout << "Height passed through from main: " << hei << "\n", c;
	cout << "The area of a 3d square is: " << area << "\n", s;
}

void QA() {
	// An input and if statement function
	string answer;
	printf("%s Which uses a TCP handshake, UDP or TCP? \n", c);
	cin >> answer; // asks answer from user
	for (auto& x : answer) { // converts ay answer into uppercase
		x = toupper(x);
	}
	cout << "Your answer is: " << answer << "\n";
	if (answer == "TCP") {
		printf("%s Correct!", s); // if answer is "TCP" then print success
	}
	else {
		printf("%s Incorrect! TCP uses a threeway handshake!", f); // Else (UDP) print incorrect
	}
}

int main() {


	cout << "Hello World! \n";
	printf("%s Everything is working... \n", s);

	int var = 15; // Assigns a number and then prints it
	cout << var << "\n";

	const double pi = 3.14;
	cout << "The first 3 digits of Pi are: \n" << pi << "\n";


	double sum = var + pi;
	cout << sum << "\n";

	multiply(5, 6, 8); // Main function responds with all integers
	QA(); // Calling function

	return EXIT_SUCCESS;
}

