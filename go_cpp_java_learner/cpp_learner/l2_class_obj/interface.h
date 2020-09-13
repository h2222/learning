// this header file includes the classes realeting to two 
// different vector classes


class vector1 
{
public:
	// class params
	double start_x;
	double start_y;
	double end_x;
	double end_y;

	// inferface functions
	void print_value();
};

// A point class that contains a single coordinate pair
class point
{ 
public:
	double x;
	double y;
};

// A vector class that has coordinate as point object
class vector2 
{
public:
	point start;
	point end;
};
