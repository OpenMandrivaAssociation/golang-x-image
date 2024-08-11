# Generated by go2rpm 1.10.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/golang/image
%global goipath         golang.org/x/image
%global forgeurl        https://github.com/golang/image
Version:                0.19.0

%gometa

%global foundry           Google
%global fontlicense       BSD
%global fontlicenses      font/gofont/ttfs/README

%global fontfamily1       Go
%global fontsummary1      A humanistic technical sans-serif font family
%global fontpkgheader1    %{expand:
Suggests:  font(gomono)
}
%global fonts1            font/gofont/ttfs/Go-*ttf
%global fontsex1          %{fonts2} %{fonts3}
%global fontconfngs1      %{SOURCE11}
%global fontdescription1  %{expand:
The Go sans-serif font family is “humanist” rather than “grotesque” in style.

The shapes of modern grotesque fonts like Helvetica are sculpted, with smooth,
assimilated forms. Humanist sans-serifs are derived from Humanist handwriting
and early fonts of the Italian Renaissance and still show subtle traces of
pen-written calligraphy. There is some evidence that humanist fonts are more
legible than grotesque fonts.

Texts set in Go occupy nearly the same space as texts in Helvetica or Arial,
but Go has a different look and texture because of its humanist style. Some Go
letters with DIN 1450 legibility features are wider than corresponding letters
in Helvetica or Arial, so some texts set in Go may take slightly more space.}

%global fontfamily2       Go Mono
%global fontsummary2      A humanistic slab-serif mono-space programming font family
%global fontpkgheader2    %{expand:
}
%global fonts2            font/gofont/ttfs/Go-Mono*ttf
%global fontconfngs2      %{SOURCE12}
%global fontdescription2  %{expand:
Go Mono has slab-shaped serifs, giving it a sturdy appearance.

The underlying letter shapes of Go Mono are, like the Go font family, derived
from humanist handwriting, but the mono-spacing and slab serifs tend to obscure
the historical and stylistic connections.

Go Mono has the same x-height as Go, 53%% of the body size. Go Mono looks almost
18% bigger than Courier, which has an x-height 45%% of body size. Yet Go Mono
has the same width as Courier, so the bigger look is gained with no loss
of economy in characters per line.

Go source code looks particularly good when displayed in Go Mono, with
punctuation characters easily distinguishable and operators lined up and placed
consistently.}


%global fontfamily3       Go SmallCaps
%global fontsummary3      The small capitals variant of the Go font family
%global fontpkgheader     %{expand:
Enhances: font(go)
}
%global fonts3            font/gofont/ttfs/Go-Smallcaps*ttf
%global fontdescription3  %{expand:
%{fontdescription1}

This variant of the Go font family provides small capitals, since they are not
exposed via standard OpenType features in the main font family.}

%global common_description %{expand:
This package holds supplementary Go image libraries.}

%global golicenses      LICENSE PATENTS
%global godocs          example AUTHORS CONTRIBUTING.md CONTRIBUTORS README.md

Name:           golang-x-image
Release:        %autorelease
Summary:        Go supplementary image libraries

License:        BSD-3-Clause
URL:            %{gourl}
Source:         %{gosource}
BuildRequires:	compiler(go-compiler)

Source11: 58-google-go-fonts.xml
Source12: 58-google-go-mono-fonts.xml

%description %{common_description}

%gopkg
%fontpkg -a
%fontmetapkg

%prep
%autopatch -p1

%build
#fontbuild -a
%gobuildroot

%install
%goinstall
#fontinstall -a

%check
%if %{with check}
%gocheck
%endif
%fontcheck -a

%gopkgfiles
%fontfiles -a
