%define		pkg	read-installed
Summary:	Read all the installed packages in a folder, and return a tree structure with all the data
Name:		nodejs-%{pkg}
Version:	2.0.5
Release:	1
License:	MIT
Group:		Development/Libraries
Source0:	http://registry.npmjs.org/%{pkg}/-/%{pkg}-%{version}.tgz
# Source0-md5:	68e9ec3c341918de23b8c9000d906daa
URL:		https://github.com/isaacs/read-installed
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
Requires:	nodejs-read-package-json < 2
Requires:	nodejs-read-package-json >= 1
Requires:	nodejs-semver < 3
Requires:	nodejs-semver >= 2
Requires:	nodejs-slide < 1.2.0
Requires:	nodejs-slide >= 1.1.3
Requires:	nodejs-util-extend < 2.0.0
Requires:	nodejs-util-extend >= 1.0.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Read all the installed packages in a folder, and return a tree
structure with all the data.

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{nodejs_libdir}/%{pkg}}
cp -a package.json %{pkg}.js $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%{nodejs_libdir}/%{pkg}
