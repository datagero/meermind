import React, { ChangeEvent } from 'react';
import { useNavigate } from 'react-router-dom';
import { styled, alpha } from '@mui/material/styles';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import InputBase from '@mui/material/InputBase';
import SearchIcon from '@mui/icons-material/Search';
import Button from '@mui/material/Button';
import { NotesAPI } from '../api/NotesAPI';
import { NoteData } from '../pages/Dashboard';

const Search = styled('div')(({ theme }) => ({
  position: 'relative',
  borderRadius: theme.shape.borderRadius,
  backgroundColor: alpha(theme.palette.common.black, 0.15),
  '&:hover': {
    backgroundColor: alpha(theme.palette.common.black, 0.25),
  },
  marginRight: theme.spacing(2),
  marginLeft: 0,
  width: '100%',
  [theme.breakpoints.up('sm')]: {
    marginLeft: theme.spacing(3),
    width: 'auto',
  },
}));

const SearchIconWrapper = styled('div')(({ theme }) => ({
  padding: theme.spacing(0, 2),
  height: '100%',
  position: 'absolute',
  pointerEvents: 'none',
  display: 'flex',
  alignItems: 'center',
  justifyContent: 'center',
}));

const StyledInputBase = styled(InputBase)(({ theme }) => ({
  color: 'inherit',
  '& .MuiInputBase-input': {
    padding: theme.spacing(1, 1, 1, 0),
    // vertical padding + font size from searchIcon
    paddingLeft: `calc(1em + ${theme.spacing(4)})`,
    transition: theme.transitions.create('width'),
    width: '100%',
    [theme.breakpoints.up('md')]: {
      width: '20ch',
    },
  },
}));

export default function SearchBar(props: { notes: NoteData[] }) {
  const [input, setInput] = React.useState('');
  const [loading,setLoading] = React.useState<Boolean>(false);
  const navigate = useNavigate();

  const handleSubmit = (event:any) => {
    event.preventDefault();
    // Handle the form submission logic
    if (!input) {
      return;
    }
    setLoading(true);
    try{
      NotesAPI.search(input).then((notes: any) => {
        setLoading(false);
      })
    }catch(e){
      console.log(e)
    }

  };

  return (
    <Box sx={{ flexGrow: 1 }}>
      <Toolbar>
        <form onSubmit={handleSubmit} style={{ display: 'flex', alignItems: 'center' }}>
          <Search>
            <SearchIconWrapper>
              <SearchIcon />
            </SearchIconWrapper>
            <StyledInputBase
              placeholder="Search…"
              inputProps={{ 'aria-label': 'search' }}
              value={input}
              onChange={(e) => setInput(e.target.value)}
            />
          </Search>
          <Button type="submit" variant="contained" color="primary">
           Search
          </Button>
        </form>
      </Toolbar>
    </Box>
  );
}
