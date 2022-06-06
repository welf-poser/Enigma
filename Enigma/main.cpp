#include<unordered_map>
#include<iostream>
#include"Enigma.h"



int main() {
	Enigma test(1, 2, 3, 1, 1, 1, 'A', "AB", "CD", "EF", "GH", "IJ", "KL", "MN", "OP", "QR", "ST");
	int test1 = 1;
	
	std::cout << test.encrypt("Seit 12 Uhr wird zurückgeschossen!!");

	return 0;
}

