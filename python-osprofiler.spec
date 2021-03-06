%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
# Created by pyp2rpm-1.1.0b
%global pypi_name osprofiler

%if 0%{?fedora} >= 24
%global with_python3 1
%endif

Name:           python-%{pypi_name}
Version:        XXX
Release:        XXX
Summary:        OpenStack Profiler Library

License:        ASL 2.0
URL:            http://www.openstack.org/
Source0:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-pbr

%description
OSProfiler is an OpenStack cross-project profiling library.

%package -n python2-%{pypi_name}
Summary:    OpenStack Profiler Library
%{?python_provide:%python_provide python2-%{pypi_name}}

Requires: python-netaddr
Requires: python-oslo-concurrency >= 3.8.0
Requires: python-oslo-log >= 3.11.0
Requires: python-oslo-messaging >= 5.2.0
Requires: python-oslo-utils >= 3.16.0
Requires: python-requests
Requires: python-six
Requires: python-webob

%description -n python2-%{pypi_name}
OSProfiler is an OpenStack cross-project profiling library.

%package doc
Summary:    Documentation for the OpenStack Profiler Library
Group:      Documentation

BuildRequires:  python-sphinx
BuildRequires:  python-oslo-sphinx
BuildRequires:  git

%description doc
Documentation for the OpenStack Profiler Library


%if 0%{?with_python3}
%package -n python3-%{pypi_name}
Summary:    OpenStack Profiler Library
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr

Requires:       python3-netaddr
Requires:       python3-oslo-concurrency >= 3.8.0
Requires:       python3-oslo-log >= 3.11.0
Requires:       python3-oslo-messaging >= 5.2.0
Requires:       python3-oslo-utils >= 3.16.0
Requires:       python3-requests
Requires:       python3-six
Requires:       python3-webob

%description -n python3-%{pypi_name}
OSProfiler is an OpenStack cross-project profiling library.
%endif


%prep
%setup -q -n %{pypi_name}-%{upstream_version}
# Let RPM handle the dependencies
rm -f requirements.txt
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif

# generate html docs
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%if 0%{?with_python3}
%py3_install
mv %{buildroot}%{_bindir}/osprofiler %{buildroot}%{_bindir}/osprofiler-%{python3_version}
ln -s ./osprofiler-%{python3_version} %{buildroot}%{_bindir}/osprofiler-3
%endif

%py2_install

%files -n python2-%{pypi_name}
%doc README.rst
%license LICENSE
%{_bindir}/osprofiler
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-*.egg-info

%files doc
%doc html
%license LICENSE

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{_bindir}/osprofiler-3
%{_bindir}/osprofiler-%{python3_version}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-*.egg-info
%endif

%changelog
