%define		kdeappsver	21.04.0
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		ktnef
Summary:	ktnef
Name:		ka5-%{kaname}
Version:	21.04.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	97d295ce658638c1c3da7a7e49344cd8
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Test-devel >= 5.9.0
BuildRequires:	Qt5Widgets-devel
BuildRequires:	gettext-devel
BuildRequires:	ka5-kcalutils-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kcalendarcore-devel >= %{kframever}
BuildRequires:	kf5-kcontacts-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The ktnef library contains an API for the handling of TNEF data. The
API permits access to the actual attachments, the message properties
(TNEF/MAPI), and allows one to view/extract message formatted text in
Rich Text Format format.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%ghost %{_libdir}/libKF5Tnef.so.5
%attr(755,root,root) %{_libdir}/libKF5Tnef.so.*.*.*
%{_datadir}/qlogging-categories5/ktnef.categories
%{_datadir}/qlogging-categories5/ktnef.renamecategories

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KTNEF
%{_includedir}/KF5/ktnef_version.h
%{_libdir}/cmake/KF5Tnef
%{_libdir}/libKF5Tnef.so
%{_libdir}/qt5/mkspecs/modules/qt_KTNef.pri
