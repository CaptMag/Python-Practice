#include <iostream>
using namespace std;

// This function passes length, width and height arguments to main()
void multiply(int len, int wid, int hei) {
	int area = len * wid * hei; // Once integers are passed, they are then multiplied
	cout << "Length passed through from main: " << len << "\n";
	cout << "Width passed through from main: " << wid << "\n";
	cout << "Height passed through from main: " << hei << "\n";
	cout << "The area of a 3d square is: " << area;
}

int main() {

	// Success and Error codes
	const char* s = "[+]";
	const char* f = "[-]";
	const char* c = "[*]";

	cout << "Hello World! \n";
	printf("%s Everything is working... \n", s);

	int var = 15; // Assigns a number and then prints it
	cout << var << "\n";

	const double pi = 3.14;
	cout << "The first 3 digits of Pi are: \n" << pi << "\n";


	double sum = var + pi;
	cout << sum << "\n";

	multiply(5, 6, 8); // Main function responds with all integers

	return EXIT_SUCCESS;
}

