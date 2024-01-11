
# Share doc between python- and python3-
%global _docdir_fmt %{name}
%global sum Google APIs Client Library for Python
%global srcname google-api-client

%if 0%{?fedora} || 0%{?rhel} > 7
%global with_python3 1
%endif

%if 0%{?rhel} > 7
%global with_python2 0
%else
%global with_python2 1
%endif

Name:           google-api-python-client
Summary:        %{sum}
Version:        1.6.5
Release:        3%{?dist}

License:        ASL 2.0
URL:            http://github.com/google/%{name}/
Source0:        https://pypi.python.org/packages/07/36/1304550b8a91e4f23258ae5880f56305528ce081cb00668107f02f153817/%{name}-%{version}.tar.gz
BuildArch:      noarch

%description 
Written by Google, this library provides a small, flexible, and powerful
Python client library for accessing Google APIs.

%if 0%{?with_python2}
%package -n python2-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python2-%{srcname}}

BuildRequires:  python2-devel >= 2.7
BuildRequires:  python2-setuptools
BuildRequires:  python2-oauth2client >= 2.0.0
BuildRequires:  python2-uritemplate >= 3.0.0

BuildRequires:  python2-httplib2 >= 0.9.2
BuildRequires:  python2-six >= 1.6.1

Requires:       python2-oauth2client >= 2.0.0
Requires:       python2-uritemplate >= 3.0.0

Requires:       python2-six >= 1.6.1
Requires:       python2-httplib2 >= 0.9.2

%description -n python2-%{srcname}
Written by Google, this library provides a small, flexible, and powerful 
Python client library for accessing Google APIs.
%endif


%if 0%{?with_python3}
%package -n python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:  python3-devel >= 3.3
BuildRequires:  python3-setuptools
BuildRequires:  python3-httplib2 >= 0.9.2
BuildRequires:  python3-oauth2client >= 2.0.0
BuildRequires:  python3-uritemplate >= 3.0.0
BuildRequires:  python3-six >= 1.6.1

Requires:       python3-httplib2 >= 0.9.2
Requires:       python3-oauth2client >= 2.0.0
Requires:       python3-uritemplate >= 3.0.0
Requires:       python3-six >= 1.6.1

%description -n python3-%{srcname}
Written by Google, this library provides a small, flexible, and powerful 
Python 3 client library for accessing Google APIs.
%endif

%prep
%setup -q

# remove egg info
rm -rf google_api_python_client.egg-info

# remove shebang without touching timestamp
for lib in googleapiclient/*.py; do
 sed '1{\@^#!/usr/bin/python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done

%build
%if 0%{?with_python2}
%{py2_build}
%endif
%if 0%{?with_python3}
%{py3_build}
%endif

%install
%if 0%{?with_python2}
%{py2_install}
%endif
%if 0%{?with_python3}
%{py3_install}
%endif

%if 0%{?with_python2}
%files -n python2-%{srcname}
%license LICENSE
%doc CHANGELOG
%{python2_sitelib}/apiclient
%{python2_sitelib}/googleapiclient
%{python2_sitelib}/google_api_python_client-%{version}-py?.?.egg-info
%endif

%files -n python3-%{srcname}
%license LICENSE 
%doc CHANGELOG
%{python3_sitelib}/apiclient
%{python3_sitelib}/googleapiclient
%{python3_sitelib}/google_api_python_client-%{version}-py?.?.egg-info

%changelog
* Tue Jun 05 2018 Troy Dawson <tdawson@redhat.com> - 1.6.5-3
- Do not do python2 in RHEL8

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Michele Baldessari <michele@acksyn.org> - 1.6.5-1
- New upstream

* Mon Oct 23 2017 Michele Baldessari <michele@acksyn.org> - 1.6.4-1
- New upstream

* Sun Sep 10 2017 Nick Bebout <nb@fedoraproject.org> - 1.6.3-2
- Fix BuildRequires/Requires to use python2-* for Fedora

* Thu Aug 31 2017 Michele Baldessari <michele@acksyn.org> - 1.6.3-1
- New upstream

* Fri Aug 4 2017 Nick Bebout <nb@fedoraproject.org> - 1.6.2-2
- Fix conditionals for epel

* Tue Aug 1 2017 Nick Bebout <nb@fedoraproject.org> - 1.6.2-1
- Update to 1.6.2

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.5.5-2
- Rebuild for Python 3.6

* Thu Nov 10 2016 Michele Baldessari <michele@acksyn.org> - 1.5.5-1
New upstream

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun May 22 2016 Michele Baldessari <michele@acksyn.org> - 1.5.1-1
- New upstream

* Thu Mar 10 2016 Michele Baldessari <michele@acksyn.org> - 1.5.0-1
- New upstream

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 31 2016 Michele Baldessari <michele@acksyn.org> - 1.4.2-4
- Make spec more epel friendly

* Mon Nov 02 2015 Michele Baldessari <michele@acksyn.org> - 1.4.2-3
- Cleanup spec according to newest python policy
- Drop python3 conditional, we'll build this for Fedora only for now anyways

* Wed Oct 21 2015 Michele Baldessari <michele@acksyn.org> - 1.4.2-2
- Address some comments from BZ 1272187

* Thu Oct 15 2015 Michele Baldessari <michele@acksyn.org> - 1.4.2-1
- Update to 1.4.2

* Tue Jun 23 2015 Michele Baldessari <michele@acksyn.org> - 1.4.1-1
- Update to 1.4.1

* Sun Jun 07 2015 Michele Baldessari <michele@acksyn.org> - 1.4.0-1
- Update to latest version
- Add python3 package
- Tag LICENSE with appropriate macro
- Generate {python,python3}-google-api-client packages to be more consistent
  within Fedora
- Add python-oauthclient dependency

* Sat Feb 14 2015 Ankur Sinha <ankursinha AT fedoraproject DOT org> 1.3.1-1
- Update to latest version

* Sat Jul 27 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 1.1-1
- Initial rpm package

