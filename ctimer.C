//=========================================================================
// Name        : timer
// Author      : wintermute
// Version     : alpha
// Copyright is gay.
// Description : a timer function
//=========================================================================
#include <Python.h>
#include <time.h>
#include <string.h>
unsigned double clock_t, flag_on, flag_off;
double elapsed;

static PyObject *    // not really sure yet... tying to pass args back and forth from timer methods?
ctimer_time(PyObject *self, PyObject *args)

{
    const char *command;
    int sts;

    if (!PyArg_ParseTuple(args, "flg", &command))
        return NULL;
    sts = system(command);
    return Py_BuildValue("clk", sts);
}



int elapsed    // working out the kinks for this method, using GNU clock
{
	
	if (flag_match_start)    // get the signal of match start
	{	
	flag_on = clock();           // start clock
	if (flag_match_end)	// end cock at match close
	{
		flag_off = clock();
		elapsed = ((double) (flag_off-flag_on)) / CLOCKS_PER_SEC;
	}		// calculate elpased time
	}
	return elapsed;
}
void turn_time()
{
	if
	



