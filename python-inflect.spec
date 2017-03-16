%global sum     Correctly generate plurals, singular nouns, ordinals, indefinite articles; convert numbers to words

Name:           python-inflect
Version:        0.2.5
Release:        1%{?dist}
Summary:        %{sum}

License:        AGPL
URL:            https://pypi.python.org/pypi/inflect
Source0:        https://pypi.python.org/packages/e1/5d/478a8e9d8b7cc004a36b75369f9caf1c23cd7ba0b97af146b516c49923d9/inflect-0.2.5.tar.gz

BuildArch:      noarch


%description
%{sum}

%package -n python2-inflect
Summary:        %sum

BuildRequires:  python2-devel
BuildRequires:  python-setuptools

Requires:       python-setuptools


%description -n python2-inflect
%{sum}


%prep
%autosetup -n inflect-%{version}


%build
%{__python2} setup.py build


%install
%{__python2} setup.py install --skip-build --root %{buildroot}


%files
%doc CHANGES.txt


%files -n python2-inflect
%{python2_sitelib}/inflect-%{version}-py*.egg-info
%{python2_sitelib}/inflect.py*


%changelog
* Thu Mar 16 2017 Tristan Cacqueray <tdecacqu@redhat.com> - 0.2.5-1
- Initial packaging
