Name:           compat-libgdata013
Version:        0.13.3
Release:        1%{?dist}
Summary:        Compat package with libgdata 0.13 libraries

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://live.gnome.org/libgdata
Source0:        http://download.gnome.org/sources/libgdata/0.13/libgdata-%{version}.tar.xz

BuildRequires:  glib2-devel libsoup-devel libxml2-devel gtk-doc intltool
BuildRequires:  gcr-devel
BuildRequires:  libgnome-keyring-devel
BuildRequires:  gnome-online-accounts-devel
BuildRequires:  gobject-introspection-devel liboauth-devel
BuildRequires:  vala-devel
BuildRequires:  vala-tools

%description
Compatibility package with libgdata 0.13 libraries.

%package -n compat-libgdata13
Summary: Compat package with libgdata 0.13 libraries
# Explicitly conflict with older libgdata packages that ship libraries
# with the same soname as this compat package
Conflicts: libgdata < 0.15

%description -n compat-libgdata13
Compatibility package with libgdata 0.13 libraries.

%prep
%setup -q -n libgdata-%{version}

%build
%configure --disable-static
make %{?_smp_mflags} CFLAGS="$CFLAGS -fno-strict-aliasing"

%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

rm -rf $RPM_BUILD_ROOT%{_includedir}
rm -rf $RPM_BUILD_ROOT%{_libdir}/girepository-1.0/
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.so
rm -rf $RPM_BUILD_ROOT%{_libdir}/pkgconfig/
rm -rf $RPM_BUILD_ROOT%{_datadir}

%post -n compat-libgdata13 -p /sbin/ldconfig

%postun -n compat-libgdata13 -p /sbin/ldconfig

%files -n compat-libgdata13
%doc COPYING
%{_libdir}/*.so.*

%changelog
* Tue Mar 17 2015 Kalev Lember <kalevlember@gmail.com> - 0.13.3-1
- libgdata compat package for el7-gnome-3-14
