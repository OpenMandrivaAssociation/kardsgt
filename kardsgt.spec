Name:           kardsgt
Version:        0.6.4
Release:        %mkrel 1
Epoch:          0
Summary:        Card game suite
License:        GPLv2+
Group:          Games/Cards
URL:            http://kardsgt.nongnu.org/
Source0:        http://download.savannah.gnu.org/releases/kardsgt/kardsgt-%{version}.tar.gz
Source1:       http://download.savannah.gnu.org/releases/kardsgt/kardsgt-%{version}.tar.gz.sig
Source2:        kardsgt.desktop
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
BuildRequires:  desktop-file-utils
BuildRequires:  ImageMagick
BuildRequires:  qt3-devel

%description
KardsGT is a card game program that has many of your favorite card 
games. Each game comes with an exhaustive manual on how to play. In 
addition to the many wonderful games, we also have amazing characters 
to play against. Each character has their own history and sense of 
play, giving you a fun challenge as you spend your time.

The specific games are:
  - cribbage
  - euchre
  - hearts
  - spades
  - war

%prep
%setup -q

%build
export QTDIR=%{_prefix}/lib/qt3
%{make}

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}
#%{__rm} -r %{buildroot}%{_datadir}/doc/kardsgt-%{version}/
%{__rm} -r %{buildroot}%{_iconsdir}/

%{__mkdir_p} %{buildroot}%{_datadir}/applications
%{_bindir}/desktop-file-install --vendor ""                         \
        --dir %{buildroot}%{_datadir}/applications                  \
        %{SOURCE2}

%{__mkdir_p} %{buildroot}%{_datadir}/pixmaps
%{_bindir}/convert -resize 32x32 src-%{version}/src/images/kardsgt.png %{buildroot}%{_datadir}/pixmaps/kardsgt.png
%{__mkdir_p} %{buildroot}%{_datadir}/icons/hicolor/16x16/apps
%{_bindir}/convert -resize 16x16 src-%{version}/src/images/kardsgt.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/kardsgt.png
%{__mkdir_p} %{buildroot}%{_datadir}/icons/hicolor/24x24/apps
%{_bindir}/convert -resize 24x24 src-%{version}/src/images/kardsgt.png %{buildroot}%{_datadir}/icons/hicolor/24x24/apps/kardsgt.png
%{__mkdir_p} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
%{_bindir}/convert -resize 32x32 src-%{version}/src/images/kardsgt.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/kardsgt.png

%clean
%{__rm} -rf %{buildroot}

%post
%{update_menus}
%{update_desktop_database}
%update_icon_cache hicolor

%postun
%{clean_menus}
%{clean_desktop_database}
%clean_icon_cache hicolor

%files
%defattr(0644,root,root,0755)
%doc ChangeLog INSTALL src-%{version}/{COPYING,INSTALL.CVS,README,CREDITS,src/NOTICE}
%attr(0755,root,root) %{_bindir}/kardsgt
%{_datadir}/applications/kardsgt.desktop
%{_datadir}/icons/hicolor/16x16/apps/kardsgt.png
%{_datadir}/icons/hicolor/24x24/apps/kardsgt.png
%{_datadir}/icons/hicolor/32x32/apps/kardsgt.png
%{_datadir}/kardsgt
%{_datadir}/pixmaps/kardsgt.png
%{_mandir}/man6/kardsgt.6*
