Nose-Gntp
==========

Nose-gntp is a nose plugin that to send notifications when a suite of tests has either succeded or failed.

## <a name="inspiration"></a>Installation

Add the following line to your requirements.txt file:

```
-e git://github.com/hurrycane/nose-gntp.git#egg=nose-gntp
```

and run pip install to install the new egg:

```
pip install -r requirements.txt 
```

When running tests add the --with-gntp flag like so:

```
nosetests --with-gntp
```

## <a name="inspiration"></a>Inspiration
[nose-gntp](https://github.com/kfdm/nose-gntp) (old)  
[nose-growl](https://bitbucket.org/osantana/nosegrowl)

Author [Bogdan](https://github.com/hurrycane)
