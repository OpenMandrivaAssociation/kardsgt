Name:           kardsgt
Version:        0.7.1
Release:        %mkrel 4
Epoch:          0
Summary:        Card game suite
License:        GPLv3+
Group:          Games/Cards
URL:            http://kardsgt.nongnu.org/
Source0:        http://download.savannah.gnu.org/releases/kardsgt/kardsgt-%{version}.tar.gz
Source1:        http://download.savannah.gnu.org/releases/kardsgt/kardsgt-%{version}.tar.gz.sig
Source2:        kardsgt.desktop
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
BuildRequires:  desktop-file-utils
BuildRequires:  imagemagick
BuildRequires:	qt4-devel
BuildRequires:	qt-assistant-adp-devel
Requires:	qt-assistant-adp
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
KardsGT is a card game program that has many of your favorite card 
games. Each game comes with an exhaustive manual on how to play. In 
addition to the many wonderful games, we also have amazing characters 
to play against. Each character has their own history and sense of 
play, giving you a fun challenge as you spend your time.

%prep
%setup -q

%build
%qmake_qt4
make
make release

%install
%{__rm} -rf %{buildroot}
make install INSTALL_ROOT=%buildroot

# install release-build binary
rm -f %buildroot%_bindir/*
install -m0755 release/%name %buildroot%{_bindir}

%{__mkdir_p} %{buildroot}%{_datadir}/applications
%{_bindir}/desktop-file-install --vendor ""                         \
        --dir %{buildroot}%{_datadir}/applications                  \
        %{SOURCE2}

%{__mkdir_p} %{buildroot}%{_datadir}/pixmaps
%{_bindir}/convert -resize 32x32 src/images/kardsgt.png %{buildroot}%{_datadir}/pixmaps/kardsgt.png
%{__mkdir_p} %{buildroot}%{_datadir}/icons/hicolor/16x16/apps
%{_bindir}/convert -resize 16x16 src/images/kardsgt.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/kardsgt.png
%{__mkdir_p} %{buildroot}%{_datadir}/icons/hicolor/24x24/apps
%{_bindir}/convert -resize 24x24 src/images/kardsgt.png %{buildroot}%{_datadir}/icons/hicolor/24x24/apps/kardsgt.png
%{__mkdir_p} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
%{_bindir}/convert -resize 32x32 src/images/kardsgt.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/kardsgt.png

%clean
%{__rm} -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_menus}
%{update_desktop_database}
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%{clean_desktop_database}
%clean_icon_cache hicolor
%endif

%files
%defattr(0644,root,root,0755)
%doc ChangeLog README CREDITS src/NOTICE
%attr(0755,root,root) %{_bindir}/kardsgt
%{_datadir}/applications/kardsgt.desktop
%{_iconsdir}/*.png
%{_iconsdir}/hicolor/*/apps/kardsgt.png
%{_datadir}/kardsgt
%{_datadir}/pixmaps/kardsgt.png
%{_mandir}/man6/kardsgt.6*


%changelog
* Sat Jul 31 2010 Funda Wang <fwang@mandriva.org> 0:0.7.1-4mdv2011.0
+ Revision: 563957
- BR qt-assistant-adp

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0:0.7.1-3mdv2010.0
+ Revision: 429660
- rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Wed Sep 24 2008 Funda Wang <fwang@mandriva.org> 0:0.7.1-2mdv2009.0
+ Revision: 287682
- requires qt4-assistant
- fix desktop file

* Wed Aug 20 2008 Funda Wang <fwang@mandriva.org> 0:0.7.1-1mdv2009.0
+ Revision: 274116
- New version 0.7.1
- gcc patch merged upstream

* Thu Aug 14 2008 Funda Wang <fwang@mandriva.org> 0:0.7.0-1mdv2009.0
+ Revision: 271751
- add patch fix gcc 4.3 building
- install release binary
- New version 0.7.0

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Tue May 06 2008 David Walluck <walluck@mandriva.org> 0:0.6.5-2mdv2009.0
+ Revision: 201746
- BuildConflicts: qt4-devel for some reason
- escape tilde in .desktop file
- fix Exec line in .desktop file (bug #40592)

* Sun Feb 03 2008 David Walluck <walluck@mandriva.org> 0:0.6.5-1mdv2008.1
+ Revision: 161631
- fix kardsgt.desktop syntax
- 0.6.5
- fix BuildRoot
- use qt3dir macro
- clean up %%install

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Funda Wang <fwang@mandriva.org>
    - drop unused condition
    - validate desktop file

* Tue Dec 25 2007 Funda Wang <fwang@mandriva.org> 0:0.6.4-1mdv2008.1
+ Revision: 137726
- clearify LICENSE
- New version 0.6.4

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Aug 05 2007 David Walluck <walluck@mandriva.org> 0:0.6.3-1mdv2008.0
+ Revision: 59025
- 0.6.3
- use %%{makeinstall_std}
- document new game
- don't ship Debian menu (rely on FDO menu)

* Fri Jun 08 2007 David Walluck <walluck@mandriva.org> 0:0.6.2-1mdv2008.0
+ Revision: 37020
- 0.6.2
- 0.6.0


* Sat Mar 17 2007 David Walluck <walluck@mandriva.org> 0.5.1-1mdv2007.1
+ Revision: 145326
- 0.5.1

* Sat Dec 30 2006 David Walluck <walluck@mandriva.org> 0:0.4.0-2mdv2007.1
+ Revision: 102761
- fix menu location

* Sat Dec 30 2006 David Walluck <walluck@mandriva.org> 0:0.4.0-1mdv2007.1
+ Revision: 102748
- fix typo
- set QTDIR
- Import kardsgt

* Sat Dec 30 2006 David Walluck <walluck@mandriva.org> 0:0.4.0-1mdv2007.1
- release

* Thu Dec 21 2006 John Schneiderman <JohnMS@member.fsf.org> 0.4.0-1jms
- SAVED GAME FILES PRIOR TO THIS RELEASE WILL NO LONGER WORK!
- New logo and player images, a default male and female image.
- Added the game of spades.
- Every player now has AI for every game.
- You can now customise the card images, and the player image.
- The screen size is now larger.
- Changed how the play sequence is shown to the player.
- You can sort the cards in your hand.
- Imrpoved the captioning system.
- Bug fix: Cribbage board no longer fails to update correctly.
- Bug fix: The default ordering in the players hand in hearts.
- Bug fix: The dialogues no longer are larger than our game screen.

* Sun Oct 15 2006 John Schneiderman <JohnMS@member.fsf.org> 0.3.0-3jms
- Added the game of hearts
- Added four new players.
- Added the ability to select the player(s) to play against.
- Now you can load game files directly from the command line with no futher intervention.
- Added turn signal indications.
- Improved the user profile database.
- Bug fix: Graphics no longer blur.
- Bug fix: Added delay so you can see the last card played.
- Bug fix: All errors are properly handled now.
- Bug fix: Card dialogues all now fit within their windows.
- Bug fix: All card message dialogues fit within their windows.
- Restructured the libraries to reduce compiling time.
- Restructured the handbook for better navigation.

* Mon Aug 07 2006 John Schneiderman <JohnMS@member.fsf.org> 0.2.0-1jms
- Cribbage game improvements and bug fixes.
- War introduced.
- Added a better looking card back image.
- Changed the game file structure, not compatible with previous versions.
- Fixed graphical bugs with KardPile and KardSequence.

* Thu Jun 08 2006 John Schneiderman <JohnMS@member.fsf.org> 0.1.0-1jms
- First Release

