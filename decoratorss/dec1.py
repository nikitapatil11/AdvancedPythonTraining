# passing argument to decorator

def decorator_with_args(decorator_args1, decorator_args2, decorator_args3, func=None):
    def decorator(func1=None):
        """

        :param func1:
        :return:
        """

        def wrapper(function_args1, function_args2, function_args3):
            print("The wrapper can access all the variables\n"
                  "\t from the decorator maker:{0} {1} {2} \n"
                  "\t from the function call:{3} {4} {5} \n"
                  "and pass them into decorator function".format(decorator_args1,
                                                                 decorator_args2,
                                                                 decorator_args3,
                                                                 function_args1,
                                                                 function_args2,
                                                                 function_args3
                                                                 ))
            return func1(function_args1, function_args2, function_args3)

        wrapper(10, 20, 30)

    decorator(func)


decorator_with_args(10, 20, 30)
