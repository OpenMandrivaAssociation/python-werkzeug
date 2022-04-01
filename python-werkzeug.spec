%global srcname Werkzeug

Name:           python-werkzeug
Version:        2.1.0
Release:        1
Summary:        The Swiss Army knife of Python web development 

Group:          Development/Python
License:        BSD
URL:            http://werkzeug.pocoo.org/
Source0:        https://pypi.python.org/packages/source/W/Werkzeug/Werkzeug-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python-sphinx
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:	python2-devel
BuildRequires:	python2-setuptools
BuildRequires:  graphviz

%description
Werkzeug
========

Werkzeug started as simple collection of various utilities for WSGI
applications and has become one of the most advanced WSGI utility
modules.  It includes a powerful debugger, full featured request and
response objects, HTTP utilities to handle entity tags, cache control
headers, HTTP dates, cookie handling, file uploads, a powerful URL
routing system and a bunch of community contributed addon modules.

Werkzeug is unicode aware and doesn't enforce a specific template
engine, database adapter or anything else.  It doesn't even enforce
a specific way of handling requests and leaves all that up to the
developer. It's most useful for end user applications which should work
on as many server environments as possible (such as blogs, wikis,
bulletin boards, etc.).

%package -n python2-werkzeug
Summary:	Summary:        The Swiss Army knife of Python web development

%description -n python2-werkzeug
Werkzeug
========

Werkzeug started as simple collection of various utilities for WSGI
applications and has become one of the most advanced WSGI utility
modules.  It includes a powerful debugger, full featured request and
response objects, HTTP utilities to handle entity tags, cache control
headers, HTTP dates, cookie handling, file uploads, a powerful URL
routing system and a bunch of community contributed addon modules.

Werkzeug is unicode aware and doesn't enforce a specific template
engine, database adapter or anything else.  It doesn't even enforce
a specific way of handling requests and leaves all that up to the
developer. It's most useful for end user applications which should work
on as many server environments as possible (such as blogs, wikis,
bulletin boards, etc.).


%prep
%setup -q -n %{srcname}-%{version}
%{__sed} -i 's/\r//' LICENSE.rst
cp -a . %py2dir
find  -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'

pushd %py2dir
find  -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python2}|'

%build
python setup.py build
find examples/ -name '*.py' -executable | xargs chmod -x
find examples/ -name '*.png' -executable | xargs chmod -x

pushd %py2dir
python2 setup.py build

%install
python setup.py install -O1 --skip-build --root %{buildroot}
export PYTHONPATH=%{buildroot}%{python_sitelib}
#%{__python} setup.py develop --install-dir %{buildroot}%{python_sitelib}

#make -C docs html

#rm -rf docs/_build/html/.buildinfo
#rm -rf examples/cupoftee/db.pyc

pushd %py2dir
python2 setup.py install -O1 --skip-build --root %{buildroot}

%files
%doc LICENSE.rst 
%{python_sitelib}/*
%doc examples

%files -n python2-werkzeug
%doc LICENSE.rst 
%{python2_sitelib}/*
%doc examples
