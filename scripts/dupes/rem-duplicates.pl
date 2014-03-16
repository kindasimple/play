#! /usr/bin/perl

use strict;
undef $/;
my $ALL = <>;
my @BLOCKS = split (/\n\n/, $ALL);

foreach my $BLOCKS (@BLOCKS) {
     my @I_FILE = split (/\n/, $BLOCKS);
     my $I;
     for ($I = 1; $I <= $#I_FILE; $I++) {
          substr($I_FILE[$I], 0,1) = '     ';
     }
     print join("\n", @I_FILE), "\n\n";
}
