# -*- coding: utf-8 -*-

def read_cfg_to_options(cfg_file='Options.ini'):
    """
    Read Options.ini file located in the ./cfg/ directory, and return an
    immutable object with fields representing the content of the ini file. The
    fields are: ['nPlayers','playerNames', 'startScores', 'qPoints1',
        'qPoints2' ,'qFileName', 'totalSpins', 'dailyDouble','timeLimit1',
        'timeLimit2', 'enableSound', 'enableAnimation']

    @type	cfg_file: string
    @param	cfg_file: path to the Options.ini

    @rtype	namedtuple
    @return	parsed INI file

    @author: J Wu, johnwuy@gmail.com
    """
    import ConfigParser, os
    from collections import namedtuple as ntp  # use nametuple since immutable

    cfg_file = os.path.join(os.getcwd(), 'wheelofjeopardy', 'cfg', cfg_file)
    cp = ConfigParser.RawConfigParser() # configParser
    tmp_name = cp.read(cfg_file) # read in config file
    if not tmp_name: # if file is not found
        raise IOError('Config file "%s" not found.' % cfg_file)

    # Parse [players] section
    sec = 'players'
    n_players = cp.getint(sec, 'numPlayers')
    player_names = [None for x in range(n_players)] # pre-allocate
    start_scores = [None for x in range(n_players)]

    for n in xrange(n_players):
        player_names[n] = cp.get(sec, 'name%d' % (n + 1))
        start_scores[n] = cp.getint(sec, 'startScore%d' % (n + 1))

    # Parse [board] section
    sec = 'board'
    daily_double = cp.getboolean(sec, 'dailyDoubleOn')
    q_points1 = [int(x) for x in cp.get(sec, 'roundOnePoints').split()]
    q_points2 = [int(x) for x in cp.get(sec, 'roundTwoPoints').split()]
    q_file_name = cp.get(sec, 'questionFile')

    # Parse [game] section
    sec = 'game'
    total_spins = cp.getint(sec, 'totalSpinsPerRound')
    enable_sound = cp.getboolean(sec, 'enableSound')
    enable_animation = cp.getboolean(sec, 'enableAnimation')
    time_limit1 = cp.getint(sec, 'round1AnswerTimeLimitInSeconds')
    time_limit2 = cp.getint(sec, 'round2AnswerTimeLimitInSeconds')

    # make the namedtuple
    options_list = [
        'n_players', 'player_names', 'start_scores', 'q_points1', 'q_points2',
        'q_file_name', 'total_spins', 'daily_double','time_limit1', 'time_limit2',
        'enable_sound', 'enable_animation'
    ]

    # make named tuple class
    Options = ntp('Options', options_list)

    # instantiate
    woj_opt = Options._make([
        n_players, player_names, start_scores, q_points1,
        q_points2, q_file_name, total_spins, daily_double, time_limit1,
        time_limit2, enable_sound, enable_animation
    ])

    return woj_opt
