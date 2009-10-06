Summary:	xmodmap application - modifying keymaps and pointer button mappings in X
Summary(pl.UTF-8):	Aplikacja xmodmap - zmiana przypisań klawiszy i przycisków myszy w X
Name:		xorg-app-xmodmap
Version:	1.0.4
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xmodmap-%{version}.tar.bz2
# Source0-md5:	bbe021f812e0014a8ee3692317788119
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-util-util-macros >= 1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The xmodmap program is used to edit and display the keyboard modifier
map and keymap table that are used by client applications to convert
event keycodes into keysyms. It is usually run from the user's session
startup script to configure the keyboard according to personal tastes.

%description -l pl.UTF-8
Program xmodmap służy do modyfikowania i wyświetlania przypisań
modyfikatorów klawiatury oraz tablicy przypisań klawiszy używanych
przez aplikacje klienckie do przekształcania kodów klawiszy zdarzenia
(keycode) na symbole klawiszy (keysym). Zwykle jest uruchamiany ze
skryptu startowego sesji użytkownika w celu skonfigurowania klawiatury
zgodnie z własnymi gustami.

%prep
%setup -q -n xmodmap-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/xmodmap
%{_mandir}/man1/xmodmap.1x*
