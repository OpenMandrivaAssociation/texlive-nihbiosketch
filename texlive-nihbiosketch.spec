Name:		texlive-nihbiosketch
Version:	54191
Release:	1
Summary:	A class for NIH biosketches based on the 2015 updated format
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/nihbiosketch
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nihbiosketch.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nihbiosketch.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX document class tries to adhere to the Biographical
Sketch formatting requirements outlined in NIH Notice
[NOT-OD-15-032]
(grants.nih.gov/grants/guide/notice-files/NOT-OD-15-032.html).
This new format is required for applications submitted for due
dates on or after May 25, 2015. The package tries to mimic the
example documents provided on the [SF 424 (R&R) Forms and
Applications page]
(grants.nih.gov/grants/funding/424/index.htm#format) as closely
as possible. The author has used this class for his own grant
submissions; however he offers no guarantee of conformity to
NIH requirements.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/nihbiosketch
%doc %{_texmfdistdir}/doc/latex/nihbiosketch

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
