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

static PyObject *
ctimer_time(PyObject *self, PyObject *args)

{
    const char *command;
    int sts;

    if (!PyArg_ParseTuple(args, "flg", &command))
        return NULL;
    sts = system(command);
    return Py_BuildValue("clk", sts);
}



int elapsed
{
	
	if (flag_match_start)
	{	
	flag_on = clock();
	if (flag_match_end)
	{
		flag_off = clock();
		elapsed = ((double) (flag_off-flag_on)) / CLOCKS_PER_SEC;
	}
	}
	return elapsed;
}
void turn_time()
{
	if
	



